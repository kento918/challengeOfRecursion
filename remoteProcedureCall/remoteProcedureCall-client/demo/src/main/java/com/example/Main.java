package com.example;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.ArrayList;

import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {
    /**
     * data.json のデータをサーバー側のメソッドを使用して答えをoutData.jsonへ書き込む
     * @param ip 相手のip
     * @param port 開放するポート
     * @param json data.jsonを受け取るクラス
     * @param jsonString data.jsonのString型
     * @param filePath data.jsonのpath
     * @param outFilePath outData.jsonのpath
     * @param serverAns サーバーからの回答をStringで受け取る
     * @param j サーバーからの回答をanswerjson型で受け取る
     * 
     * サーバー側で準備しているメソッドについて
     * 以下のメソッドについてサーバーで処理することができる。
     *   メソッド名|         引数型| 返り値型
     *        floor|         double|  double
     *        nroot|      [int,int]|  double
     *      reverse|         String|  String
     * validAnagram|[String,String]| boolean
     *         sort|       String[]|  String
     */
    public static void main(String[] args){
        String ip = "192.168.0.30";
        int port = 55535;
        sendJson json = new sendJson();
        ObjectMapper mapper = new ObjectMapper();
        String jsonString = "";
        String filePath = "D:\\user\\connectingForPython_json\\demo\\src\\main\\resources\\data.json";
        String outFilePath = "D:\\user\\connectingForPython_json\\demo\\src\\main\\resources\\outData.json";
        try{
            //filePath からjsonのオブジェクトを作成後Stringを作る
            Path f = FileSystems.getDefault().getPath(filePath);
            json= mapper.readValue(f.toFile(),sendJson.class);
            
            jsonString = json.toString();
        } catch (IOException e) {
            new IOException("");
        }
        //TCPを使用してjsonを送信し、答えをoutData.json.dataへ書き込む
        try(Socket sock = new Socket(ip, port)) { 
            try(
            PrintWriter writer = new PrintWriter(sock.getOutputStream(),true);
            BufferedReader reader = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            FileWriter w = new FileWriter(new File(outFilePath));
            ){
                writer.println(jsonString); 
                writer.flush();
                
                String serverAns = reader.readLine();
                serverAns = checkJsonString(serverAns); 
                answerJson j = mapper.readValue(serverAns , answerJson.class);
                String ansJson =  mapper.writerWithDefaultPrettyPrinter().writeValueAsString(j);
                ansJson = checkJsonString(ansJson);
                w.write("{"+ansJson+"}");
            }
        }catch(UnknownHostException e){
           System.out.println(e);
        }catch(IOException e){
           System.out.println(e);
        }
    }
    /**pythonから送信されたStringデータを一部編集して読み込める形へ変えていく
     * pythonからのStringデータにはエスケープシーケンスの\が含まれているため、削除する。
     * また、{}についても削除する必要があったので最後に除いたStringを返している。
    */
    private static String checkJsonString(String serverAns) {
        if(serverAns.isEmpty()){
            return "param:null";
        }
        System.out.println(serverAns);
        String ans = "";
        ArrayList<String> list = new ArrayList<>(); 
        for(int i = 0; i < serverAns.length(); i++){
            if(serverAns.charAt(i) != '\\') list.add(String.valueOf(serverAns.charAt(i)));
        }
        for(String a : list) ans += a;
        return ans.substring(1,ans.length()-1);
    }
}