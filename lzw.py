
import sys

#LZW Compress function

def compress():
  inputStr = raw_input('please input code input:')
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
#LZW Decompress
def decompress():
 
 
    inputStr = raw_input('please input code input:')
    inputStrArray = inputStr.split()
    inputIntArray = [int(i) for i in inputStrArray]
    
    hints = ['curCode', 'oldCodeStr', 'isCurCodeInDict', 'curCodeStr', 'addedDictItem']
    print hints[0].ljust(20), hints[1].ljust(20), hints[2].ljust(20), hints[3].ljust(20)\
    , hints[4].ljust(20)
 
 
    ans = curCodeStr = oldCodeStr = ''
    dicSize = 3
    isCurCodeInDict = True
    dict = {1:'a', 2:'b', 3:'c'}

    for curCode in inputIntArray:
        if curCode  in dict:
            curCodeStr = dict[curCode]
            isCurCodeInDict = True
        else:
            #2
            curCodeStr = oldCodeStr + oldCodeStr[0]
            isCurCodeInDict = False
            
        if oldCodeStr != '':
            dicSize = dicSize + 1
            dict[dicSize] = oldCodeStr + curCodeStr[0]
        
        print str(curCode).ljust(20), oldCodeStr.ljust(20), str(isCurCodeInDict).ljust(20)\
        , curCodeStr.ljust(20), str(dicSize) + ':' + dict[dicSize]
        
        oldCodeStr = curCodeStr
        ans = ans + curCodeStr
        
    print ans
    
#Main function
if __name__ == "__main__":
    compress()
    decompress():
