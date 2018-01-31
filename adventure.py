#Caleb Callaway
#1/31/18
#adventure.py - uses if statements to mimic the computer game adventure


name = input("Choose your name. ")
year = input("what year is it?")

print ("Well,",name,", unfortunately you are lost in a Costco.")

first = input("Do you stay where you are and crack open a crate of Coke?")

if first == "yes":
    print ("Good choice!")
    second = ("You see an employee. Do you wave them down and ask for help?")
    if second == yes:
        print ("Oooooh... bad move. Never ask for help. YOU LOSE. RIP",name,", died",year.")