#12. Find the GCD of two numbers using a loop

# n1=int(input("Enter num"))
# n2=int(input("Enter num"))
# gcd=1
# for i in range(1,min(n1,n2)+1):
#     if(n1%i==0 and n2%i==0):
#      gcd=i

# print("GCD is :",gcd)







n1=int(input("Enter num:"))
n2=int(input("Enter num:"))
gcd=1

for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print("GCD is:",gcd)