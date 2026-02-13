# 2. Create a function to return factorial of a number

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact


# num = int(input("Enter a number: "))
# print("Factorial is:", factorial(num))
  


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

num=int(input("Enter a num:")) 
print("Factorial is :",factorial(num))   
