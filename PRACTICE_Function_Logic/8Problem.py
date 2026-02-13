# 10. Write a recursive function for sum of digits.


def sum_of_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_of_digits(num // 10)

# Example
n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))






 