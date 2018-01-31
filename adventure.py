#Caleb Callaway
#1/31/18
#adventure.py - uses if statements to mimic the computer game adventure


name = input("Choose your name. ")
year = input("what year is it?")

print ("Well,",name,", unfortunately you are lost in a Costco.")

first = input("Do you stay where you are and crack open a crate of Coke? ")

if first == "yes":
    print ("Good choice!")
    second = input("You see an employee. Do you wave them down and ask for help? ")
    if second == "yes":
        print ("Oooooh... bad move. Never ask for help. YOU LOSE. RIP",name,", died",year)
    elif second == "no":
        print ("Well done! Assistance is for the weak.")
        third = input ("You start to get tired. Do you try and stay awake by drinking more Coke? ")
        if third == "yes":
            fourth = input("All that coke is making you feel sick. You throw up. Gross! Do you try to clean it up? ")
        elif third == "no":
            print ("You fall asleep, and while you're sleeping the store closes.")
            fourth = input("Do you try to make your way to the door so you'll be found when they open? ")
            if fourth == "yes":
                print("While you were stumbling through the dark, you tripped and fell into the depths of Hell.")
                fifth == input("Do you want to climb out? ")
                if fifth == "yes":
                    print("Well you can't. YOU LOSE. RIP",name,", died",year.)
                elif fifth == "no":
                    sixth = input("Satan comes up to you, but he doesn't see you. Do you want to greet him?")
                    if sixth == "yes":
                        print ("You say 'Hi Satan', and he's really pleased that you're so friendly. You and Satan become best pals forever. YOU WIN!")
                    elif sixth == "no":
                        print ("Your rudeness will get you nowhere. Satan notices you hiding behind a rock and chops you up into little pieces. YOU LOSE. RIP",name,", died",year.)
                
elif first == "no":
    print ("Sounds like a bad plan to me, but whatever.")
    second = input ("Do you want to try and find your way out?")
    if second =="yes":
        third = input ("Do you want to try and retrace your steps?")
        if third == "yes":
            print ("Oh, rough- you retraced somebody else's steps by accident. They led you into the bathroom where you died of gas asphyxiation.")
        elif third == "no":
            fourth = input ("OK, well, uh, do you want to just, like, run around and hope for the best?")
            if fourth == "yes":
                print ("Oh! Wow! There's the front door! I was not expecting that to work, but, uh, good job! YOU WIN")
            elif fourth == "no":
                fifth == input ("Well, uh, what do you wnat to do?")
                print("Wrong! Your decision was so bad that you just exploded right in the middle of the hardware aisle. YOU LOSE. RIP",name,", died",year.)
    elif second == "no":
        third = input ("Do you want to try and establish an overnight shelter?")
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        