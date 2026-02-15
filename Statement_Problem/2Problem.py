# 7. Write a Python program to check whether  the given
#              number is an Armstrong number or not. 


num=int(input("Enter a number: "))

temp=num
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if sum==num:
    print(num,"is an Armstrong num.")
else:
    print(num,"is Not an Armstrong num.")  
          

 

