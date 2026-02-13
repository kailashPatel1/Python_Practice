# 9. Create a function that returns maximum of three numbers.



# def ram(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
    
# a=int(input("Enter the 1st num:"))    
# b=int(input("Enter the 2nd num:"))    
# c=int(input("Enter the 3rd num:"))   


# print("Greatest Number is: ",ram(a,b,c))




def maximum(a,b,c):
    if(a>b and a>c):
        return a
    
    elif(b>a and a>c):
        return b
    else:
        return c

a=int(input("Enter your num1:"))    
b=int(input("Enter your num2:"))    
c=int(input("Enter your num3:"))    

print("Greater num is :",maximum(a,b,c))


