# 3. Remove all punctuation or spaces from a string.


# import string
# text = input("Enter a string: ")

# # Remove spaces
# noSpace = text.replace(" ", "")

# print("String after removing punctuation and spaces:", noSpace)



# name=input("Enter your name:")
# space=(name.replace(" ",""))
# print("After removing space:",space)







str=input("Enter string:")
space=str.replace(" ","")
print("After removing space:",space)




# String Palindrome

str=input("Enter a string:")
if str==str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")    
 

