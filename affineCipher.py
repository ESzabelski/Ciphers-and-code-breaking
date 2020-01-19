#Affine Cipher
#uses multiplication and addition to crypt messages

import sys, pyperclip, cryptomath, random
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
    myMessage=  "'A computer would deserve to be called intelligent if it could deceive a human into believing that it was human.' -Alan Turning"
    #myMessage="rU!oR9lO6iL3fIzcFwZCtW.qT nQ8kN5hK2eHybEvYBsV?pS0mP7jM4gJ1dGxaDuXA"
    myKey=2111
    myMode='encrypt' #set to encrypt or decrypt

    if myMode=="encrypt":
        translated=encryptMessage(myKey,myMessage)
    elif myMode=="decrypt":
        translated=decryptMessage(myKey,myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print("Full %sed text copied to clipboard" %(myMode))

def getKeyParts(key):
    keyA=key//len(SYMBOLS)
    keyB=key%len(SYMBOLS)
    return (keyA,keyB)

def checkKeys(keyA,keyB,mode):
    if keyA==1 and mode=="encrypt":
        sys.exit("Cipher is weak if key A is 1, pick a different one") #try with this removed
    if keyB==0 and mode=="encrypt":
        sys.exit("Cipher is weak if key B is 0, pick a different one")
    if keyA<0 or keyB<0 or keyB>len(SYMBOLS)-1:
        sys.exit("Key A must be above 0, B between 0 and symbol length")
    if cryptomath.gcd(keyA, len(SYMBOLS))!=1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA,len(SYMBOLS)))
                
def encryptMessage(key,message):
    keyA,keyB=getKeyParts(key)
    checkKeys(keyA,keyB,"encrypt")
    ciphertext=""
    for symbol in message:
        if symbol in SYMBOLS:
            #encrypt the symbol
            symbolIndex=SYMBOLS.find(symbol)
            ciphertext+=SYMBOLS[(symbolIndex*keyA +keyB) %len(SYMBOLS)] #this is the primary part of the Affine cipher
        else:
            ciphertext+=symbol
    return ciphertext

def decryptMessage(key,message):
    keyA,keyB=getKeyParts(key)
    checkKeys(keyA,keyB,"decrypt")
    plaintext=""
    modInverseOfKeyA=cryptomath.findModInverse(keyA,len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            #decrypt
            symbolIndex=SYMBOLS.find(symbol)
            plaintext+=SYMBOLS[(symbolIndex - keyB)*modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext+=symbol
    return plaintext

def getRandomKey():
    while True:
        keyA=random.randint(2,len(SYMBOLS))
        keyB=random.randint(2,len(SYMBOLS))
        if cryptomath.gcd(keyA,len(SYMBOLS))==1:
            return keyA*len(SYMBOLS)+keyB

#checks if program ran or main

if __name__=="__main__":
    main()




























        




    
