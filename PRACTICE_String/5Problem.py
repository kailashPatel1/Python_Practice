# # 5. Check if two strings are anagrams.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# # Remove spaces and convert to lowercase
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()

# # Check if sorted characters are the same
# if sorted(str1) == sorted(str2):
#     print("✅ The strings are anagrams.")
# else:
#     print(" The strings are not anagrams.")






# #################  


str1=input("Enter a sting:")
str2=input("Enter a string:")

str1=str1.replace(" ","").upper()
str2=str2.replace(" ","").upper()

if sorted(str1)==sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")    


