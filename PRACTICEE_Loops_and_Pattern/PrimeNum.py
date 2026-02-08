#9 Check whether a number is prime using a loop.


# n = int(input("Enter your num: "))

# for i in range(2,n):
#     if n%i==0:
#         print("Not Prime")
#         break
# else:
#     print("num is Prime")    












n=int(input("Enter a num:"))

for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print(" prime.")

