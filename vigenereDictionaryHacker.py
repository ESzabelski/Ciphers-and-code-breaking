#tries the Vigenere Cipher by forcing every common dictionary word

import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext="""Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage!= None:
        print("copying hacked message to clipboard")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print("Failed to hack the encryption")

def hackVigenereDictionary(ciphertext):
    fo = open("dictionary.txt")
    words=fo.readlines()
    fo.close()

    for word in words:
        word=word.strip() #removes the newline at end
        decryptedText=vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText,40): #sends 40% as the 2nd argument
            #checks if it is right
            print()
            print("Possible answer:")
            print("Key " +str(word) + ": " + decryptedText[:100])
            print()
            print("Press D for done or enter to continue")
            response=input(">")

            if response.upper().startswith("D"):
                return decryptedText

if __name__=="__main__":
    main()
