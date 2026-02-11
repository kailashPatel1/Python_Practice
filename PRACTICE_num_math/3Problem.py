# num = int(input("Enter a number: "))
# rev = 0

# while num != 0:
#     digit = num % 10        # Get last digit
#     rev = rev * 10 + digit  # Add digit to reversed number
#     num = num // 10         # Remove last digit

# print("Reversed number:", rev)




# Second method for reverse the digit:

n=int(input("Enter a num:"))
while n>0:
    r=n%10
    print(r,end="")
    n=n//10

