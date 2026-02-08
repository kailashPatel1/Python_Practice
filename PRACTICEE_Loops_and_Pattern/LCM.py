# Find the LCM of two numbers using a loop.

# n1=int(input("Enter a num:"))
# n2=int(input("Enter a num:"))

# if(n1>n2):
#     greater=n1
# elif n2>n1:
#     greater=n2

# while True:
#     if(greater%n1==0 and greater%n2==0):
#         break
#     greater=greater+1
    
# print("LCM is:",greater)                













n1=int(input("Enter your num:"))
n2=int(input("Enter your num:"))

if(n1>n2):
    greater=n1
elif(n2>n1):
    greater=n2

while True:
    if(greater%n1==0 and greater%n2==0): 
        break
    greater=greater+1

print("LCM is:",greater)       


