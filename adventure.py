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
            if fourth == "yes":
                print ("Ugh!")
                print ("You're too late! the scent of the coke vomit attracts Costco wolves, who devour you. YOU LOSE. RIP",name,", died",year)
            elif fourth == "no":
                print ("You move to a new area.")
                fifth = input ("Do you want to go to sleep and wait for help? ")
                if fifth == "yes":
                    print ("Wrong! Assistance is for the weak! YOU LOSE.")
                elif fifth == "no":
                    sixth = input("Do you want to use your survival skills from the Scouts to make it through the night? ")
                    if sixth == "yes":
                        print ("Uhh, you were never a boy scout...? What were you thinking? YOU LOSE. RIP",name,", died",year)
                    elif sixth == "no":
                        print ("Well that's dumb.")
        elif third == "no":
            print ("You fall asleep, and while you're sleeping the store closes.")
            fourth = input("Do you try to make your way to the door so you'll be found when they open? ")
            if fourth == "yes":
                print("While you were stumbling through the dark, you tripped and fell into the depths of Hell.")
                fifth = input("Do you want to climb out? ")
                if fifth == "yes":
                    print("Well you can't. YOU LOSE. RIP",name,", died",year)
                elif fifth == "no":
                    sixth = input("Satan comes up to you, but he doesn't see you. Do you want to greet him? ")
                    if sixth == "yes":
                        print ("You say 'Hi Satan', and he's really pleased that you're so friendly. You and Satan become best pals forever. YOU WIN!")
                    elif sixth == "no":
                        print ("Your rudeness will get you nowhere. Satan notices you hiding behind a rock and chops you up into little pieces. YOU LOSE. RIP",name,", died",year)
            elif fourth == "no":
                print ("You're going to need shelter to avoid dying of exposure.")
                fifth = input ("Do you want to try sleeping under this foam mat you found on one of the shelves? ")
                if fifth == "yes":
                    sixth = input ("You sleep out the night. Do you want to try and leave Costco, now that it's open? ")
                    if sixth == "yes":
                        print ("Well. You got out. Good job. YOU WIN!!")
                    elif sixth == "no":
                        print ("You remain in Costco, dwelling among the shelves and feeding off of mislaid food crates. You become hairy, like a baboon, and you begin hallucinating giant butterflies and caterpillars.")
                        seventh = input ("NOW do you want to leave? ")
                        if seventh == "yes":
                            print ("Well you can't. It is too late. YOU ARE THE COSTCO BEAST NOW")
                        elif seventh == "no":
                            print ("You have accepted your role as the Costco Beast. You will live in harmony with the crates forever. YOU WIN!!")
                elif fifth == "no":
                    print ("You died of exposure. I told you you needed shelter. Way to go, champ. YOU LOSE. RIP",name,", died",year)
                
elif first == "no":
    print ("Sounds like a bad plan to me, but whatever.")
    second = input ("Do you want to try and find your way out? ")
    if second =="yes":
        third = input ("Do you want to try and retrace your steps? ")
        if third == "yes":
            print ("Oh, rough- you retraced somebody else's steps by accident. They led you into the bathroom where you died of gas asphyxiation. YOU LOSE. RIP",name,", died",year)
        elif third == "no":
            fourth = input ("OK, well, uh, do you want to just, like, run around and hope for the best? ")
            if fourth == "yes":
                print ("Oh! Wow! There's the front door! I was not expecting that to work, but, uh, good job! YOU WIN")
            elif fourth == "no":
                fifth = input ("Well, uh, what do you want to do?")
                print("Wrong! Your decision was so bad that you just exploded right in the middle of the hardware aisle. YOU LOSE. RIP",name,", died",year)
    elif second == "no":
        third = input ("Do you want to try and establish an overnight shelter? ")
        if third == "yes":
            fourth = input ("Do you want to gather some good construction materials instead of using empty coke bottles?")
            if fourth == "yes":
                fifth = input("There's plywood or styrofoam. The wood is really heavy. Do you want it anyway? ")
                if fifth ==  "yes":
                    print ("You had no trouble carrying the wood, but it took you so long that night fell and you blindly stumbled into the landmine aisle and died on the demonstration floor. YOU LOSE. RIP",name,", died",year) 
                elif fifth == "no":
                    print ("The styrofoam is so light that when a draft blows through the Costco, the styrofoam acts like a hang glider and you fly up above all the shelves.")
                    sixth == input("Do you want to try flying out the windows? ")
                    if sixth == "yes":
                        print ("You should know that most Costcos don't have windows. You crashed into the wall and died instantly. YOU LOSE. RIP",name,", died",year)
                    elif sixth == "no":
                        seventh = input ("Do you want to land on a shelf? ")
                        if seventh == "yes":
                            print ("You landed on a shelf, where you were found and rescued the next morning by an employee restocking the baby wipes. YOU WIN!")
                        elif seventh == "no":
                            print ("You flew around for so long that you died of dehdration. YOU LOSE. RIP",name,", died",year)
            elif fourth == "no":
                print ("The empty Coke bottles you used are great at insulating, but they are hard to build a fort out of.")
                fifth = input ("Do you want stuff your clothes with bottles to make a warm Coke suit? ")
                if fifth == "yes":
                    print ("You were found in the morning, but were mistaken for a new species of gorilla and mde to spend the rest of your days in a zoo. YOU LOSE. RIP",name,", died in a zoo.")
                elif fifth == "no":
                    print ("You were unable to make a bottle fort and you died of exposure. YOU LOSE. RIP",name,", died",year)
        elif third == "no":
            print ("Well, night fell, and you are starting to get hypothermia since you have no shelter.")
            fourth = input ("Do you want to build a fire to keep warm?")
            if fourth == "yes":
                fifth= input("You have matches. Do you want to try and find a lighter in the store instead, to save matches? ")
                if fifth == "yes":
                    print ("Oh no! You got lost and froze to death. The costco mice nibble at your bleached bones. YOU LOSE. RIP",name,", died",year)
                elif fifth == "no":
                    print ("You started a fire, tripping the store's alarm. Firemen following the smoke found you sitting there and rescued you. YOU WIN!!")
            elif fourth == "no":
                ("You froze to death, dipstick! Why didn't you make a fire? YOU LOSE. RIP",name,", died",year)
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
