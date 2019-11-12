# detect english module
#to use type this code:
# import detectEnglish, then detectEnglish.isEnglish(astring) and returns true/false
#also uses dictionary.txt file with words one per line

UPPERLETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE=UPPERLETTERS+UPPERLETTERS.lower() +" \t\n"

def loadDictionary():
    dictionaryFile=open("dictionary.txt")
    englishWords={}
    for word in dictionaryFile.read().split("\n"):
        englishWords[word]=None     #creates  a dict, with each key's value as none
    dictionaryFile.close()
    return englishWords



ENGLISH_WORDS=loadDictionary()

def getEnglishCount(message):
    message=message.upper()
    message=removeNonLetters(message)
    possibleWords=message.split()

    if possibleWords==[]:
        return 0.0

    matches=0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches+=1
    return float(matches)/len(possibleWords)

def removeNonLetters(message):
    lettersOnly=[]
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)

def isEnglish(message, wordPrecentage=20, letterPercentage=85):
    #sets a default of 20% words and 85% letters
    wordsMatch=getEnglishCount(message)*100>=wordPrecentage
    numLetters=len(removeNonLetters(message))
    messageLettersPercentage=float(numLetters)/len(message)*100
    lettersMatch=messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
    

