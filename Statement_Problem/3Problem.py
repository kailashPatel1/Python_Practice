# WAP of Leap Year


year=int(input("Enter the Year:"))

if year%400==0:
    print(year,"is a leap year.")
elif year%100==0:
    print(year,"is not leap year.")
elif year%4==0:
    print(year,"is leap year.")    
else:
    print(year,"not leap year.")

