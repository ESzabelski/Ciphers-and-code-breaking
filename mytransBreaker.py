import math
#     0...4...8...2...6...0...4...8       
msg=("Cenoonommstmme oo snnio. s s c")
key=8
def breaker (astr,key):

    #len is 29, so needs to get to 32

    l=len(astr)

    rounded=math.ceil(l/key)#so 4 in eg
    iterate_rate=rounded
    #key=8
    
    #total message length
    tml=rounded*key

    newstring=""
    for i in range (0,rounded):
        for x in range(0,key-1): #this is one short of end so 7
            #FIRST LOOP IS I =0
            #SO I NEED 0,4,8
            index=(i+x*rounded)
            #print(index)
            newstring=newstring+astr[index]
            
        value=(key*rounded)-(1+(rounded-i))
        if value<l:

            newstring=newstring+astr[value]
            print(newstring,"XXXX")
    print(newstring)  
            

##    for i in range(0,len(astr),key):
##        #1 +iterater-rate until tml then add 1
##        print(i)


breaker(msg,key)

    
