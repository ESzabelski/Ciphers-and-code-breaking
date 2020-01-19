#Frequency finder, counts how many encrypted letters appear in a text

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
# Returns a dictionary with keys of single letters and values of the
# count of how many times they appear in the message parameter:
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
           'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
           'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
           'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter]+=1

    return letterCount

def getItemAtIndexZero(items):
    return items[0]

def getFrequencyOrder(message):
    #returns a string of alphabet letters arranged in order of most
    #frequently occuring in the message

    #First gets a dictionary of each letter and its frequency count
    letterToFreq=getLetterCount(message)

    #next makes a dictionary of each frequnecy count to the letters with that frequnecy
    freqToLetter={}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]]=[letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    #third, put the letters in reverse ETAOIN order
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq]="".join(freqToLetter[freq])

    #fourth convert this dictionary to a list of tuples, then sort
        freqPairs=list(freqToLetter.items())
        freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    #fifth now they are ordered, extract them for the final string
    freqOrder=[]
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
    return "".join(freqOrder)


def englishFreqMatchScore(message):
    #return the number of matches in this message compared to the order
    #of english letters.  A match is top 6 or bottom 6 letters matching
    freqOrder=getFrequencyOrder(message)
    matchScore=0
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore+=1
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore+=1
    return matchScore
            
