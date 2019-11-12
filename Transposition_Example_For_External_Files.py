#transposition cipher encrypt and decrypt external files
#switch between encrypt and decrypt modes

import time, os, sys, transpositionEncrypt, transposition_decrypt

def main():
    inputFilename= "frankenstein.txt"
    outputFilename="frankenstein.encrypted.txt"

    #decryptexample:
##    inputFilename= "frankenstein.encrypted.txt"
##    outputFilename="f_decrypt.txt"

    
    myKey=10
    myMode= "encrypt" #switch to encrypt/decrypt if needed

    #test if input files is present
    if not os.path.exists(inputFilename):
        print("the file %s does not exist.  Quitting." % (inputFilename))
        sys.exit()

    #checks if output file already exists and gives a chance to exit
    if os.path.exists(outputFilename):
        print ("This will overwrite file %s  (C)ontinue or (Q)uit?" % (outputFilename))
        response=input("> ")
        if not response.lower().startswith("c"):
            sys.exit()

    fileObj=open(inputFilename)
    content=fileObj.read()
    fileObj.close()

    print("%sing..."% (myMode.title()))

    #test how long process takes

    startTime=time.time()
    if myMode=="encrypt":
        translated=transpositionEncrypt.encryptMessage(myKey,content)
    elif myMode=="decrypt":
        translated=transposition_decrypt.decryptMessage(myKey, content)
    totalTime=round(time.time() - startTime,2)
    print("%sion time: %s second" %(myMode.title(),totalTime))

    #write message to output file
    outputFileObj=open(outputFilename,"w")
    outputFileObj.write(translated)
    outputFileObj.close()

    print("done %sing %s (%s characters)."%(myMode, inputFilename,len(content)))
    print("%sed file is %s. " % (myMode.title(), outputFilename))

#if run instead of as module, call the main
if __name__=="__main__":
    main()
    
    
