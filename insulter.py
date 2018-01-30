#Caleb Callaway
#1/30/18
#insulter.py- uses random numbers to insult the user


from random import randint

num = randint(1,5)

name = input("What's your name?")

if num == 1:
    print ("Seriously? Your face could scare a vulture away from a pile of animal carcasses.")
    
elif num == 2:
    print ("Who taught you English? An octopus?")
    
elif num == 3:
    print ("Aw, well aren't you special and unique. People must like you a lot.")
    
elif num == 4:
    print ("what's your e-mail,",name,",",name,"@biggiantloser.com?")
    
elif num == 5:
    print ("Jeez, how did your mother feed you without getting close enough to smell you?")