# Find the Greatest Common Divisor (GCD) of two numbers

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# gcd=1

# for i in range(1,min(a,b)+1):
#     if(a%i==0 and b%i==0):
#         gcd=1
#         print("GCD is:",gcd)





# n1=int(input("Enter num 1st:")) 
# n2=int(input("Enter num 2nd:"))

# gcd=1 
# for i in range(1,min(n1,n2)+1):
#     if(n1%i==0 and n2%i==0):
#         gcd=1  
#         print("GCD is:",gcd)  




n1=int(input("Enter a num:"))
n2=int(input("Enter a num:"))
gcd=1
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print("GCD is:",gcd)
           
