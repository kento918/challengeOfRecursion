package com.example;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown=true)
public class answerJson {
   String results;
   String result_type;
   String[] resultArr;
   int id;

   public answerJson(String results , String result_type , int id){
      this.results = results;
      this.result_type = result_type;
      this.id = id;
   }
   public answerJson(String[] resultArr , String result_type , int id){
      this.results = null;
      this.resultArr = resultArr;
      this.result_type = result_type;
      this.id = id;
   }

   public answerJson(){
      
   }

   public String getResults(){
      return this.results;
   }

   public String getResult_type(){
      return this.result_type;
   }

   public int getId(){
      return this.id;
   }
}


// public static answerJson createAnsJson(){

// }