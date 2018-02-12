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
    
    
    
if "p" or "P" in word1 and if "p" or "P" in word2:
    print ("These words both have p's.")
    
if "p" or "P" in word1:
    print (word1,"has at least 1 p.")
    
if "p" or "P" in word2:
    print (word2,"has at least 1 p.")