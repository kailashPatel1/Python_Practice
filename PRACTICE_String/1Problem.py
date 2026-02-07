# 1. Count uppercase, lowercase, digits, and special characters

# text = input("Enter any string: ")
# upper = 0
# lower = 0
# digit = 0
# special = 0

# for kp in text:
#     if kp.isupper():
#         upper += 1
#     elif kp.islower():
#         lower += 1
#     elif kp.isdigit():
#         digit += 1
#     else:
#         special += 1



# print("Uppercase letters:", upper)   
# print("Lowercase letters:", lower)
# print("Digits:", digit)
# print("Special characters:", special)



##### ek bar jo raghubar ki najro ka sahara ho jayeeksmsdkdld
   
##########################

str=input("Enter a string:")
upper=0
lower=0
digit=0
special=0
for x in str:
    if x.isupper():
        upper=upper+1
    elif x.islower():
        lower=lower+1
    elif x.isdigit():
        digit=digit+1
    else:
        special=special+1
print("Upper Case:",upper)                 
print("Lower Case:",lower)                 
print("Digits:",digit)                  
print("Special Characters",special)                 







