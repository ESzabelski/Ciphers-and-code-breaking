#Affine cipher hacke

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE=False

def main():

    myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage= hackAffine(myMessage)

    if hackedMessage !=None:
        #displays message and copies to clipboard

        print("Copied to clipboard")
        print(hackedMessage)
    else:
        print("Failed to hack encryption")

def hackAffine(message):
    print("Hacking...")
    print("Press cntl + c to quit at any time")

    for key in range(len(affineCipher.SYMBOLS) **2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA,len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key,message)
        if not SILENT_MODE:
            print("Tried key %s (%s)" %(key, decryptedText[:40]))
        if detectEnglish.isEnglish(decryptedText):
            #asks user if this is right key
            print()
            print("Possible hack:")
            print(decryptedText[:200])
            print()
            print("Press 'd' if done")
            response=input(">")

            if response.strip().upper().startswith("D"):
                return decryptedText
    return None


if __name__== '__main__':
    main()
    
