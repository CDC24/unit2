#Caleb Callaway
#1/30/18
#compoundDemo.py- how to use and/or

num = int(input("Enter a number. "))

if num>0 and num%7==0:
    print(num,"is positive and divisible by 7! Good.")

elif num>0:
    print(num,"is positive but not divisible by 7. RIP.")
    
elif num<0 and num%7==0:
    print(num,"is negative and divisible by 7. I guess.")
    
elif num<0:
    print(num,"is negative and not divisible by 7. Huh.")
    
else:
    print (num,"is zero. what a bore-fest.")