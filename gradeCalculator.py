#Caleb Callaway
#1/29/18
#gradeCalculator.py - uses if statements to change a grade percentage to a letter grade


grade = int(input("What is your grade? "))

if grade >= 90:
    print ("You got an A.")
elif grade >= 80:
    print ("You got a B.")
elif grade >= 70:
    print ("You got a C.")
elif grade >= 60:
    print ("You got a D.")
elif grade < 60:
    print ("You got an F :(")
