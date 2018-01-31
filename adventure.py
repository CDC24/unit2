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
    if second == "no":
        print ("Well done! Assistance is for the weak.")
        third = input ("You start to get tired. Do you try and stay awake by drinking more Coke?")
        if third == "yes":
            fourth = input("All that coke is making you feel sick. You throw up. Gross! Do you try to clean it up?")
        if third == "no":
            fourth = input("You fall asleep