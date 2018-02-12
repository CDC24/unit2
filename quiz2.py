# Caleb Callaway
# 2/12/18
# quiz2.py- unit 2 quiz


words = input ("enter two words: ")

word1, word2 = words.split( )

if len(word1)>len(word2):
    print (word1,"is a longer word than",word2)

elif len(word2)>len(word1):
    print (word2,"is a longer word than",word1)
    
else:
    print ("These words are the same length.")
    
    
    
if word1.count("p" or "P")>=1 and word2.count("p")>=1:
    print ("These words both have p's.")
    
elif word1.count("p" or "P")>=1:
    print (word1,"has at least 1 p.")
    
elif word2.count("p" or "P")>=1:
    print (word2,"has at least 1 p.")
    
print ("Now is addition time.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1+num2==12:
    print ("Correct! These numbers add to 12!")
else:
    print ("False! These numbers add to",num1+num2)