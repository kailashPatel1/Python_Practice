# Write a function to reverse the digits of a number without converting it to a string.

n=int(input("Enter the num:"))  

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10        
        rev = rev * 10 + digit       
        num //= 10                   
    return rev

# Example

n = 12345
print("Reversed number:", reverse_number(n))


