import sys
 
def compress():
  inputStr = input('please input code input:')
  hints = ['prefix', 'curChar', 'curStr', 'isCurStrInDict', 'addedDictItem', 'output']
    print hints[0].ljust(20), hints[1].ljust(20), hints[2].ljust(20), hints[3].ljust(20)\
    , hints[4].ljust(20), hints[5].ljust(20)
 
 
    prefix = curChar = curStr = output = ans = ''
    isCurStrInDict = False
    dict = {'a':1, 'b':2, 'c':3}
    
    for curChar in inputStr:
        curStr = prefix + curChar
        print prefix.ljust(20), curChar.ljust(20), curStr.ljust(20),
        if curStr in dict:
            output = ''
            isCurStrInDict = True
            prefix = curStr

        else:
            output = str(dict[prefix])
            isCurStrInDict = False
            prefix = curChar
            dict[curStr] = len(dict) + 1


        print str(isCurStrInDict).ljust(20),    
        
        if isCurStrInDict:
            print ''
        else:
            print str(curStr+':'+str(dict[curStr])).ljust(20), output.ljust(20)
        
        if output != '':
            ans = ans + ' ' + output
        
    output = str(dict[prefix])        
    print prefix.ljust(20), 'empty'.ljust(20), prefix.ljust(20), 'True'.ljust(20)\
    , ''.ljust(20), output.ljust(20)
    ans = ans + ' ' + output
    print ans

if __name__ == "__main__":
    compress()
