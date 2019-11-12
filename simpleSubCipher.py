#makes a simple substition cipher
#change to encrypt or decrypt

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():

    
    myMode="decrypt"  #change here
    myMessage = """If a man is offered a fact which goes against his
          instincts, he will scrutinize it closely, and unless the evidence
          is overwhelming, he will refuse to believe it. If, on the other
          hand, he is offered something which affords a reason for acting
          in accordance to his instincts, he will accept it even on the
          slightest evidence. The origin of myths is explained in this way.
          -Bertrand Russell"""
    myKey = getRandomKey()


    if not keyIsValid(myKey):
        sys.exit("there was an error in the key or symbol set")

    #determines which function to follow    
    if myMode=="encrypt":
        translated=encryptMessage(myKey,myMessage)
    elif myMode=="decrypt":
        translated=decryptMessage(myKey,myMessage)

    print("Using are currently using key %s" %(myKey))
    print("The %sed message is:" %(myMode))
    print()
    print(translated)
    pyperclip.copy(translated)
    print()
    print("this has been copied to the clipboard")

def keyIsValid(key):
    keyList=list(key)
    lettersList=list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList==lettersList #check wheter you have 26 letters in each

def encryptMessage(key,message):
    return translateMessage(key,message,"encrypt")

def decryptMessage(key,message):
    return translateMessage(key,message,"decrypt")

def translateMessage(key,message,mode):
    translated=""
    charsA=LETTERS
    charsB=key
    if mode=="decrypt":
        #for decrypting you can use same letters, just swap them
        charsA,charsB=charsB,charsA

    #loops each symbol in message to encrypt or decrypt
    for symbol in message:
        if symbol.upper() in charsA: #this skips spaces, puncuation etc
            symIndex=charsA.find(symbol.upper())#sets index to then swap below

            
            if symbol.isupper():
                translated+=charsB[symIndex].upper()
            else:
                translated+=charsB[symIndex].lower()
        else:
            #for symbols not in letters, just add them
            translated+=symbol
    return translated

def getRandomKey():
    key=list(LETTERS)
    random.shuffle(key)
    return "".join(key)

if __name__=="__main__":
    main()


    
