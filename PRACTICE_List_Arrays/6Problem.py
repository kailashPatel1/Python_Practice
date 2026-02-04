# 7. Separate even and odd numbers from a list.

# lst=[1,2,4,5,6,8,9,12,13]

# even=[]
# odd=[]

# for num in lst:

#   if (num%2==0):
#     even.append(num)
#   else:
#     odd.append(num)  

# print("even num:",even)   
# print("odd num:",odd) 





lst=[2,3,6,7,9,1,8]
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)    
print("Even num:",even)
print("Odd num:",odd)

