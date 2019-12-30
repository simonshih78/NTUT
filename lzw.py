import sys
'''
NTUT DATA Compression course
107368527 Simon 
'''
#LZW Compress function

def compress():
    inputStr = raw_input('encode input:')
    hints = ['prefix-code', 'curChar', 'curStr', 'flag', 'insert2DICT', 'outcome']
    prefix = ''
    curChar= ''
    curStr = '' 
    output = ''
    ans = ''
    flag = False
    dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5\
            ,'f':6, 'g':7, 'h':8, 'i':9, 'j':10\
            ,'k':11, 'l':12, 'm':13, 'n':14, 'o':15\
            ,'p':16, 'q':17, 'r':18, 's':19, 't':20\
            ,'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26\
           } 
  
 
    print hints[0].ljust(20)+hints[1].ljust(20)+hints[2].ljust(20)+hints[3].ljust(20)+hints[4].ljust(20)+hints[5].ljust(20)     

    for curChar in inputStr:
        curStr = prefix + curChar
        print prefix.ljust(20), curChar.ljust(20), curStr.ljust(20),
        if curStr in dict:
            output = ''
            flag = True
            prefix = curStr

        else:
            output = str(dict[prefix])
            flag = False
            prefix = curChar
            dict[curStr] = len(dict) + 1


        print str(flag).ljust(20),    
        
        if flag:
            print ''
        else:
            print str(curStr+':'+str(dict[curStr])).ljust(20), output.ljust(20)
        
        if output != '':
            ans = ans + ' ' + output
        
    output = str(dict[prefix])        
    print prefix.ljust(20), 'empty'.ljust(20), prefix.ljust(20), 'True'.ljust(20), ''.ljust(20), output.ljust(20)
    ans = ans + ' ' + output
    print "final output:"+str(ans)

#LZW Decompress
def decompress():
    inputStr = raw_input('decode input:')
    inputStrArray = inputStr.split()
    inputIntArray = [int(i) for i in inputStrArray]
    hints = ['prefix-code', 'curChar','flag', 'insert2DICT', 'outcome']
    print hints[0].ljust(20)+hints[1].ljust(20)+hints[2].ljust(20)+hints[3].ljust(20)+hints[4].ljust(20)     
    ans = ''
    curCodeStr = ''
    oldCodeStr = ''
    dicSize = 3
    isCurCodeInDict = True
    dict = {1:'a', 2:'b', 3:'c'}

    
    for curCode in inputIntArray:
        if curCode  in dict:
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
    print "final output:"+str(ans)
    
#Main function
if __name__ == "__main__":
    mode = raw_input('please input mode: (encode/decode)')
    if mode == "encode":
        compress()
    elif mode == "decode":
        decompress()
    else:
        print("please enter correction string.")
        exit -1
