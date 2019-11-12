#simulates an auto test of the other two programs, calling them both into play and giving
#random seeds and tests.

import random, sys, transpositionEncrypt, transposition_decrypt

def main():
    random.seed(42)

    for i in range(20):

        message="ABCDEFGHIJKLMNOPQRSTUVWXYZ" *random.randint(4,40)

        #converts to list then shuffles it
        message=list(message)
        random.shuffle(message)
        message="".join(message)

        print('Test #%s: "%s..." ' % (i + 1, message[:50]))

        for key in range (1,int(len(message)/2)):
            encrypted=transpositionEncrypt.encryptMessage(key,message)
            decrypted=transposition_decrypt.decryptMessage(key,encrypted)

            #if it doesnt match display error
            if message!=decrypted:
                print ("mismatch with key %s and message %s" %(key, message))
                print ("decrypted as"+decrypted)
                sys.exit()
    print("transposition cipher passed")

#if run instead of module
if __name__=="__main__":
    main()
    

            
