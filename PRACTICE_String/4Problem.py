# 4. Replace vowels in a string with a symbol (*).


# text = input("Enter a string: ")    

# vowels = "AEIOUaeiou"
# result = ""

# for ch in text:
#     if ch in vowels:
#         result += "*"
#     else:
#         result += ch
# print("String after replacing vowels:", result)



############

# txt=input("Enter a string:")
# vowels="aeiouAEIOU"
# result=""
# for k in txt:
#     if k in vowels:
#         result=result+"*"
#     else:    
#        result=result+k
# print("String after replacing vovels:",result)        




txt=input("Enter string:")
vowels="aeiouAEIOU"
result=" "
for k in txt:
    if k in vowels:
        result=result+"*"
    else:
        result=result+k
print("String after replacing vowels:",result)    



   