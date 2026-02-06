# 4. Find key with maximum value in dictionary. 


# . Prime Number Check
 
# num=int(input("Enter the number:"))

# for i in range(2,num):
#     if num % i ==0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")





 

# Check Palindrome


# s=input("Enter String:")

# if s==s[::-1]:
#     print("Palindrome")

# else:
#     print("Not Palindrome")    




# Armstrong Number


# n = int(input("Enter number: "))
# s = str(n)
# total = sum(int(d)**3 for d in s)

# if total == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")





# a=input("Enter the string:")

# if a==a[::-1]:
#     print("palindrom")
# else:
#     print("Not Polindrom")    





# Remove Duplicates from List

# lst=[1,3,2,1,4,3,1]
# d=[]
# for x in lst:
#     if  x not in d:
#         d.append(x)
# print(d)






# Find Max & Min Without Built-in

# lst=[2,4,34,3]

# maxi=lst[0]
# mini=lst[0]

# for x in lst:
#     if x > maxi:
#         maxi=x
#     if x < mini:
#         mini=x
# print("max:",maxi)     
# print("min",mini)    
# #  


 

# # Merge Multiple Dictionaries

# a = {"p": 1}
# b = {"q": 2}
# c = {"r": 3}

# merged = a | b | c
# print(merged)






# # second method to merged
# d1 = {'a':1, 'b':2}
# d2 = {'c':3, 'd':4}

# d3 = {**d1, **d2}
# print(d3)



# # Find Key with Maximum Value

# d = {'a':10, 'b':25, 'c':15}

# m = max(d, key=d.get)
# print(m)













# Prime num

# num=int(input("Enter your num:"))
# for i in range(2,num):
#     if(num%i==0):
#         print("Not prime")
#         break
# else:
#     print(f"{num} is prime")





# Find Max & Min Without Built-in


lst=[2,4,34,3]

maxi=lst[0]
mini=lst[0]

for x in lst:
    if x > maxi:
        maxi=x
    if x < mini:
        mini=x
print("max:",maxi)     
print("min",mini)    



# 

lst=[2,4,12,8,3,11,15,18]
maximum=lst[0]
minimun=lst[0]
for x in lst:
    if x>maximum:
        maximum=x
    if x<minimun:
        minimun=x
print("maximum num is:",maximum)        
print("minimum num is:",minimun) 

 


