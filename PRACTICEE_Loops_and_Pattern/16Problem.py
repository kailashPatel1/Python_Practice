# Count vowels and consonants in a string using a loop.

# str=input("Enter a string:")
# vowels=0
# consonants=0
 
# for ch in str:
#     if ch.isalpha():
#         if ch.lower()in "aeiou":
#             vowels=vowels+1
#         else:
#             consonants +=1
# print("Vowels:",vowels)   
# print("Consonants:",consonants) 




str=input("Enter your string:")
vowel=0
conso=0
for ch in str:
    if ch.lower() in "aeiou":
        vowel=vowel+1
    else:
        conso=conso+1
print("vowel is:",vowel)    
print("Consonants is:",conso)  


