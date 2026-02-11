#Check if a number is a Perfect number

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")


