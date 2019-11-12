


import math, pyperclip

def main():
    myMessage="Cenoonommstmme oo snnio. s s c"
    myKey=8

    plaintext=decryptMessage(myKey,myMessage)

    print(plaintext)

    pyperclip.copy(plaintext)


def decryptMessage(key,message):
    #simulates columns and rows

    #columns
    numOfColumns=int(math.ceil(len(message)/float(key)))
    numOfRows=key
    numOfShadedBoxes=(numOfColumns*numOfRows)-len(message)

    plaintext=[""]*numOfColumns

    column=0
    row=0

    for symbol in message:
        plaintext[column] += symbol
        #plaintext[column]=plaintext[column]+symbol
        column=column+1

        #if no more columsn or shaded box to back to first and new row
        if (column==numOfColumns) or (column==numOfColumns-1 and row>=numOfRows - numOfShadedBoxes):
            column=0
            row=row+1
    return "".join(plaintext)


if __name__=='__main__':
    main()
