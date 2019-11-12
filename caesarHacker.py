#hack the ceasar cyphyer

message = "avnl1olyD4l'ylDohww6DhzDjhuDil,"
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#try changing the symbol and see if it still works      
for key in range(len(SYMBOLS)):
    translated=''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            translatedIndex=symbolIndex - key

            #wrap around

            if translatedIndex<0:
                translatedIndex=translatedIndex+len(SYMBOLS)

            translated=translated+SYMBOLS[translatedIndex]

        else:
            translated=translated+symbol

    #print all kinds
    print('key #%s: %s' %(key, translated))
