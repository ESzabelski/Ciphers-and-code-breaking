#a hack program for the vigenere cipher


import itertools, re
import vigenereCipher, pyperclip, freqAnalysis, detectEnglish

LETTERS =" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SILENT_MODE = False #(If True, program doesnt print anything)
NUM_MOST_FREQ_LETTERS = 4 #attempt to keep this many letters per subkey
MAX_KEY_LENGTH= 16 #will not try longer than this

NONLETTERS_PATTERN= re.compile("[^A-Z]")

def main():
    
    ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
    hackedMessage = hackVigenere(ciphertext)


    if hackedMessage!=None:
        print("Copying hacked message:")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print("Failed to hack encryption")

def findRepeatSequencesSpacings(message):
    #Goes through the message and finds 3-5 letter sequences that are repeated
    #returns a dictionary with keys of the sequence and values of a list of spacing
    #(num of letters between the repeats)

    #use a regulat expression to remove non-letters
    message=NONLETTERS_PATTERN.sub("",message.upper())

    #compilea list of seqLen-letter sequence found in the message
    seqSpacings={} #keys are the sequence
    for seqLen in range(3,6):
        for seqStart in range(len(message)-seqLen):
            #determine sequence and store it in seq
            seq=message[seqStart:seqStart + seqLen]
            #look for this in rest of message
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i+seqLen]==seq:
                    #found a repeat
                    if seq not in seqSpacings:
                        seqSpacings[seq]=[] #init a blank list

                    #append the space between the repeat sequence
                        #and the oringinal sequence
                    seqSpacings[seq].append(i-seqStart)
    return seqSpacings

def getUsefulFactors (num):
    #returns a list of useful factors by num.  Useful means less than
    #max key length. eg 144: 2,3,4,6,8,9,12,16

    if num<2:
        return [] # no useful factor
    factors=[]

    #only check to max key length
    for i in range(2,MAX_KEY_LENGTH+1):
        if num% i==0:
            factors.append(i)
            otherFactor=int(num/i)
            if otherFactor< MAX_KEY_LENGTH +1 and otherFactor!=1:
                factors.append(otherFactor)
    return list(set(factors))


def getItemAtIndexOne(items):
    return items[1]


def getMostCommonFactors(seqFactors):
    #first get count of how many times a factor occurs
    factorCounts={} #key is factor, value is how many times it occurs

    # seqFactors keys are sequences, values are lists of factors of the
    # spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
    # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}

    for seq in seqFactors:
        factorList=seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor]=0
            factorCounts[factor]+=1
    #2nd, put factor and count in a tuple, make a list
    factorsByCount=[]
    for factor in factorCounts:
        if factor <= MAX_KEY_LENGTH:
            #fbc has a value like (factor, factorcount) eg [ [3,293],[2,411]}
            factorsByCount.append( ( factor, factorCounts[factor]))
    #sort the list
    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount



def kasiskiExamination(ciphertext):
        # Find out the sequences of 3 to 5 letters that occur multiple times
    # in the ciphertext. repeatedSeqSpacings has a value like:
    # {'EXG': [192], 'NAF': [339, 972, 633], ... }
    #repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)
    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

    # (See getMostCommonFactors() for a description of seqFactors.)
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    # (See getMostCommonFactors() for a description of factorsByCount.)
    factorsByCount = getMostCommonFactors(seqFactors)

    # Now we extract the factor counts from factorsByCount and
    # put them in allLikelyKeyLengths so that they are easier to
    # use later:
    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])

    return allLikelyKeyLengths



def getNthSubkeysLetters(nth, keyLength, message):
    # Returns every nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

    # Use a regular expression to remove non-letters from the message:
    message=NONLETTERS_PATTERN.sub("",message)

    i = nth -1
    letters=[]
    while i < len(message):
        letters.append(message[i])
        i+=keyLength
    return "".join(letters)




def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    #determines the most likely key length
    ciphertextUp=ciphertext.upper()

    #allFreqScores is a list of the mostlikelykeylength number of lists
    #these inner lists the the freqscore list
    allFreqScores=[]
    for nth in range(1,mostLikelyKeyLength+1):
        nthLetters=getNthSubkeysLetters(nth,mostLikelyKeyLength, ciphertextUp)
        
        # freqScores is a list of tuples like:
        # [(<letter>, <Eng. Freq. match score>), ... ]
        # List is sorted by match score. Higher score means better match.
        # See the englishFreqMatchScore() comments in freqAnalysis.py.
        freqScores = []

        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        #sort by match score            
        freqScores.sort(key=getItemAtIndexOne, reverse=True)

        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

    if not SILENT_MODE:
        for i in range (len(allFreqScores)):
            #i+1 so first isn't '0th' letter
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print("%s " %freqScore[0], end="")
            print()

    #try every combination of the most likely letters for each posistion in the key
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
    #creates possible key from letters in all FreqScore:
        possibleKey=""
        for i in range(mostLikelyKeyLength):
            possibleKey+= allFreqScores[i][indexes[i]][0]

        if not SILENT_MODE:
            print("Attempting with key: %s" % (possibleKey))
        decryptedText=vigenereCipher.decryptMessage(possibleKey, ciphertextUp)

        if detectEnglish.isEnglish(decryptedText):
            #set it to oringinal capitalization
            origCase=[]
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText="".join(origCase)

            # Check with user to see if the key has been found:
            print('Possible encryption hack with key %s:' % (possibleKey))
            print(decryptedText[:200]) # Only show first 200 characters.
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')
                        
            if response.strip().upper().startswith('D'):
                return decryptedText

    # No English-looking decryption found, so return None:
    return None

def hackVigenere(ciphertext):
    # First, we need to do Kasiski Examination to figure out what the
    # length of the ciphertext's encryption key is:
    allLikelyKeyLengths = kasiskiExamination(ciphertext)
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('Kasiski Examination results say the most likely key lengths are: ' + keyLengthStr + '\n')
    hackedMessage = None
    for keyLength in allLikelyKeyLengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
        if hackedMessage != None:
            break

    # If none of the key lengths we found using Kasiski Examination
    # worked, start brute-forcing through key lengths:
    if hackedMessage == None:
        if not SILENT_MODE:
            print('Unable to hack message with likely key length(s). Brute forcing key length...')
        for keyLength in range(1, MAX_KEY_LENGTH + 1):
            # Don't re-check key lengths already tried from Kasiski:
            if keyLength not in allLikelyKeyLengths:
                if not SILENT_MODE:
                    print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
                hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                if hackedMessage != None:
                    break
    return hackedMessage

#if run instead of import as a module:

if __name__=="__main__":
    main()




    

