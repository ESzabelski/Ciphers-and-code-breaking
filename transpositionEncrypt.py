

import pyperclip

def main():
    #myMessage= "Common sense is not so common."
    myMessage="""Ryla was humming to herself, happy despite the desolation outside, staring out of the thick window at the small energy fields fighting in desperation to keep the paths clear against the extreme amounts of snow from last night.  In contrast the sun was out, giving the frosted landscape a nice aesthetic touch to the otherwise bleak desolation.  She sighed.  She did not like the cold, the snow, or dark so perhaps this was a very bad place for her but these kinds of mornings gave her a sort of strength to remain joyful. Her main job was head of communications – which might seem strange given her slightly introverted nature, but her shyness never interfered with her duties – but she was also trained in flying aerial vehicles.  She was learning how to fly the Gyro-Copter from Feyria since things pretty slow on Reiko-10 at the moment.  Today would be perfect to practice some more since the weather was supposed to be clear for the first half of the day.  If she could only pull Feyria away from the guys… Yeah that sounded like a plan.  Feyria was amazing at flying and would gladly help Ryla further.  Ryla went to turn to leave her slight daydream when she felt a claw dig into her right shoulder."""

    myKey=22

    ciphertext=encryptMessage(myKey,myMessage)

    #print end along with pipe
    print(ciphertext+'|')  
    pyperclip.copy(ciphertext)

def encryptMessage(key,message):
    #string represents a column in grid
    ciphertext=['']*key

    #loop through each column
##    for column in range(key):
##        currentIndex=column  #ie 0,1,2
##        while currentIndex < len(message):
##            #place the characterat currentindex in the messag at the end
##            #of the current colum in ciphertext list
##            ciphertext[column]+=message[currentIndex]
##
##            #move index over
##            currentIndex+=key  #why isnt this 1?


##    for column in range(key):
##        currentIndex=column  #ie 0,1,2
##        while currentIndex < len(message):
##            ciphertext[column]+=message[currentIndex]
##            #move index over
##            currentIndex+=key  #why isnt this 1?
##            

    for i in range(key):
        x=i
        while x < len(message):
            ciphertext[i]=ciphertext[i]+message[x]
            x=x+key  #why isnt this 1? >because it has to skip through all letters back to column
            #so this works by copying x to i, because x has to be modified 'more locally' , like 1,5,9, before i becomes 2, so then its 2,6,10            

            
    #convert list to single string
    return ''.join(ciphertext)


#if file is run instead of imported as module call the main function

#if __name__ == '__main__':
#    main()
main()
