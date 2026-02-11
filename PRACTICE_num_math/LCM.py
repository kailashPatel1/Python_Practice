# LCM:-
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     greater = a
# else:
#     greater = b

# while True:
#     if (greater % a == 0) and (greater % b == 0):
#         lcm = greater
#         break
#     greater += 1

# print("LCM of", a, "and", b, "is:", lcm)





n1=int(input("Enter a num:"))
n2=int(input("Enter a num:"))

if n1>n2:
    greater=n1
elif n2>n1:
     greater=n2

while True:
     if greater%n1==0 and greater%n2==0:
          break
     greater=greater+1
print("LCM is:",greater)



    
   




 
