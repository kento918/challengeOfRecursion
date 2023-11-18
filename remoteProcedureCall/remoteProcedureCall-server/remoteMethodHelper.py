import decimal

def choiceMethod(method , *tuppleNums):
    if(method == 'floor'):
        return floor(tuppleNums[0])
    elif(method == 'nroot'):
        return nroot(tuppleNums[0], tuppleNums[1])
    elif(method == 'reverse'):
        return reverse(tuppleNums[0])
    elif(method == 'validAnagram'):
        return validAnagram(tuppleNums[0] , tuppleNums[1])
    elif(method == 'sort'):
        return sort(tuppleNums[0])
    return method +  ' end'

def choiceMethodSort(param):
    return sort(param)

def floor(x):
    return decimal.Decimal(x).quantize(decimal.Decimal('0'),rounding=decimal.ROUND_HALF_EVEN)

def nroot(n,x):
    return pow(n,1/x)

def reverse(strings):
    newStr =''
    for x in range(0,len(strings)):
        newStr = strings[x] + newStr
    return newStr

def validAnagram(first , second):
    for x in range(0,len(first)):
        for y in range(0,len(second)):
            if(first[x] == second[y]):
                second = second.replace(first[x] , '' , 1)
                break
    return len(second) == 0

def sort(strArr):
    return sorted(strArr)
    

def changeType(zips):
    newlist = []
    for paramslist, typeslist in zips:
        if(typeslist == 'int'):
            newlist.append(int(paramslist))
        elif(typeslist == 'double'):
            newlist.append(float(paramslist))
        elif(typeslist == 'String'):
            newlist.append(str(paramslist))
    return newlist

def createJsonString(ans, id):
    if(type(ans) is int):
        anstype = 'int'
        return "{{\"results\":\"{0}\",\"result_type\":\"{1}\",\"id\":{2}}}" .format(ans , anstype , id)
    elif(type(ans) is float):
        return "{{\"results\":\"{0}\",\"result_type\":\"{1}\",\"id\":{2}}}" .format(ans , 'double' , id)
    elif(type(ans) is bool):
        return "{{\"results\":\"{0}\",\"result_type\":\"{1}\",\"id\":{2}}}" .format(ans , 'boolean' , id)
    elif(type(ans) is list):
        return "{{\"results\":\"{0}\",\"result_type\":\"{1}\",\"id\":{2}}}" .format(ans , 'String[]' , id)
    else:
        anstype = 'String'
        return "{{\[\"results\":\"{0}\",\"result_type\":\"{1}\",\"id\":\"{2}\"\]}}" .format(ans , anstype , id)