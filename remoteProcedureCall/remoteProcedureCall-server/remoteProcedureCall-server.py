import socket
import json
import os
import remoteMethodHelper

x = 2
y = 4

port = 55535 
ip = '192.168.0.30'

mainPCAddress = {ip , port}

def textToJson(text):
    result = ''
    for x in range(0,len(text)):
        if(text[x] == '[') and (text[x-1] =='\"'):
            result = result[0:len(result)-1] + text[x]
        elif(text[x] == '\"') and (text[x-1] == ']'):
            continue
        else:
            result = result + text[x]
    return result

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# sock.close()
sock.bind(('0.0.0.0' , port))
sock.listen(1)

while True:
    print('connection start')
    connection , address = sock.accept()
    data = connection.recv(1024)
    datastr = data.decode('utf-8')
    
    print('client>' , datastr)
        
    jsondata = json.loads(textToJson(datastr))
    print(jsondata)
    method = jsondata.get('method')
    beforzipparams = jsondata.get('params')
    beforzipparamtypes = jsondata.get('param_type')
    id = jsondata.get('id')
    # print(beforzipparams)
    # print(beforzipparamtypes)
    # print(id)
    if(method == 'sort'):
        ans = remoteMethodHelper.choiceMethodSort(beforzipparams)
        answerJsonString = remoteMethodHelper.createJsonString(ans , id)
    else:
        zips = zip(beforzipparams, beforzipparamtypes)
        params = remoteMethodHelper.changeType(zips)
        ans = remoteMethodHelper.choiceMethod(method, *params)
        answerJsonString = remoteMethodHelper.createJsonString(ans, id)
    print('json is ' + answerJsonString)
    connection.send(json.dumps(answerJsonString).encode('utf-8'))
    print('send a message' + answerJsonString)  
    with open('./ans.json', 'w') as jsons: 
        json.dump(answerJsonString,jsons , indent=2)
    
    connection.close()
sock.close()