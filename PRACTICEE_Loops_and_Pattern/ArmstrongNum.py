# Check whether a number is an Armstrong number.

n=int(input("Enter a num:"))
temp=n
sum=0

while n>0:
    r=n%10
    sum=sum+r*r*r
    n=n//10

if temp==sum:
    print("Armstrong Num")    
else:
    print("Not Armstrong.")    


