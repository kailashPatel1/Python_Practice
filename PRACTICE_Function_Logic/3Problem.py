# 3. Write a function to return Fibonacci up to n terms

# def fibonacci(n):
#     fib = []
#     a, b = 0, 1

#     for k in range(n):
#         fib.append(a)
#         a, b = b, a + b

#     return fib

# print(fibonacci(10)) 




# def fibonacci(n):
#     fib=[]
#     a,b=0,1

#     for k in range(n):
#         fib.append(a)
#         a,b=b,a+b
#     return fib
# print(fibonacci(15))    




def fibo(n):
    fib=[]
    a=0
    b=1
    for k in range(n):
        fib.append(a)
        a,b=b,a+b
    return fib
print(fibo(10))    


