# Number Palindrome using logic

# n=int(input("Enter a number:"))
# temp=n
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n//=10
# if temp==rev:
#     print("Num is Palindrome.")
# else:
#     print("Not Palindrome")





# Prime num:

n=int(input("Enter num:"))
for i in range(2,n):
    if n%i==0:
        print("Not Prime.")
        break
else:
 print("Prime num.")    




