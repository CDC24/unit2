#Caleb Callaway
#1/29/18
#movie.py - uses if statements to tell if user of specific age can watch certain movie ratings

age = int(input("what is your age? "))

if age >= 18:
    print ("You could watch up to NC-17 movies.")
elif age >=13:
    print ("You could watch up to PG-13 movies, or R movies if accompanied by an adult guardian or parent. ")
else:print ("You could watch up to PG-13 movies if reviewed by an adult guardian or parent. ")