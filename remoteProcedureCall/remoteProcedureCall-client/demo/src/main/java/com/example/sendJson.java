package com.example;

public class sendJson {
   String method;
   String[] params;
   String[] param_types;
   int id;
   public String getMethod(){
      return this.method;
   }
   public String[] getParams(){
      return this.params;
   }
   public String[] getParam_types(){
      return this.param_types;
   }
   public int getId(){
      return this.id;
   }
   public void setMethod(String method){
      this.method = method;
   }
   public void setParams(String[] Params){
      this.params = Params;
   }
   public void setParam_types(String[] type){
      this.param_types = type;
   }
   public void setId(int id){
      this.id = id;
   }

   public String toString(){
      String param1 = getArrayString(params);
      String param2 = getArrayString(param_types);
      return String.format("{\"method\" : \"%s\",\"params\" : \"%s\",\"param_type\" : \"%s\",\"id\" : \"%d\"}" , this.method , param1 , param2 , this.id);
   }
   
   public String getArrayString(String[] arr){
      String ans ="";
      for(int i = 0; i < arr.length;i++){
         ans += String.format("\"%s\", " , arr[i]);
      }
      ans = "[" + ans.substring(0,ans.length()-2) + "]";
      return ans;
   }
}
