
# Check if a number is a Strong number (sum of factorials of digits equals the number).

num = int(input("Enter a number: "))
temp = num 
sum = 0 

while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    num //= 10

if sum == temp:
    print(temp, "is a Strong number")
else:
    print(temp, "is not a Strong number")

