#Vigenere Cipher (Multi-alphabetic substitution cipher)

import pyperclip
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    myKey="ASIMOV"
    myMode="decrypt" #set to encrypt or decrypt

#This way works and is cleaner, but other programs use some functions, so this
#doesnt work in those cases
##    
##    if myMode == 'encrypt':
##        translated = translateMessage(myKey, myMessage,"encrypt")
##    elif myMode == 'decrypt':
##        translated = translateMessage(myKey, myMessage,"decrypt")
##
##    print('%sed message:' % (myMode.title()))
##    print(translated)
##    pyperclip.copy(translated)
##    print()
##    print('The message has been copied to the clipboard.')
##
##def encryptMessage(key, message):
##    return translateMessage(key, message, 'encrypt')
##
##def decryptMessage(key, message):
##    return translateMessage(key, message, 'decrypt')


    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')




###
def translateMessage(key, message, mode):
    translated=[]

    keyIndex=0
    key=key.upper()
    for symbol in message:
        num=LETTERS.find(symbol.upper())
        if num!= -1: #-1 means symbol wasnt found
            if mode =="encrypt":
                num+= LETTERS.find(key[keyIndex]) #adds if encypting

            elif mode== "decrypt":
                num-= LETTERS.find(key[keyIndex]) #subtracts for decypting


            num %=len(LETTERS) #for wraparound

            #adds the symbols together
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex +=1 #moves to next letter in key
            if keyIndex==len(key):
                keyIndex=0
        else:
            #append symbol without changing it
            translated.append(symbol)
    return "".join(translated)

if __name__=="__main__":
    main()

