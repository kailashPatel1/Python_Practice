# # Check whether a number is a palindrome using a loop.

# n=int(input("Enter num:"))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10

# if temp==sum:
#     print("Polindrom num")
# else:
#     print("Not polindrom.")    




# Second method ,Check whether a number is a palindrome using string.



# n = input("Enter your number: ")

# if n == n[::-1]:
#     print("Palindrome number")
# else:
#     print("Not palindrome")




n=input("Enter num:")
if n==n[::-1]:
    print("Polindrom")
else:
    print("not polindrom")    


