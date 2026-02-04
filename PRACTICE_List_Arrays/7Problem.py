# Rotate List by K

# lst=[1,2,3,5,4]
# k=3
# k=k%len(lst)
# rotated=lst[k:] + lst[:k]
# print(rotated)

# lst=[2,3,3,2,2,]
# a=2
# k=k%len(lst)
# r=lst[k:]+lst[:k] 
# print(r)



lst=[5,3,3,2,2,5]
checks=[]       

for x in lst:
    if x  not in checks:
        checks.append(x)
 
print(checks)       


 