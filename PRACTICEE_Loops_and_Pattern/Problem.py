# 7.Count the number of digits in a number.

# n = int(input("Enter number: "))
# count = 0

# while n > 0:
#     count += 1
#     n //= 10

# print("Number of digits:", count)



#8 Find the sum of digits of a number.

n=int(input("Enter num:"))
s=0
while n> 0:
    s+=n%10
    n//=10
print("Sum of digits:",s)




