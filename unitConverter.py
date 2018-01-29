#Caleb Callaway
#1/29/18
#unitConverter.py - uses if statements to allow user to choose a conversion type and perform it

print ("Which conversion would you like to perform? 1)Kilometers to meters, 2)Kilograms to pounds, 3)Liters to gallons, or 4)Celsius to Fahrenheit")
conversion = input("Enter the number of the conversion you would like to perform. ")

if conversion == 1:
    km = float(input("Enter a number of kilometers: "))
    print (km,"Km =",km*0.621371192,"miles.")
elif conversion == 2:
    print ("um OK")