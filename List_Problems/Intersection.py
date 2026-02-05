
#9.Intersection of two lists:
lst1=[2,5,8,7,9,4]
lst2=[3,4,5,6,7,8,9]
intersection=[]

for i in lst1:
    for j in lst2:
        if i==j:
            intersection.append(i)
print("Intersection is :",intersection)            



# Unioun of two list:
lst1=[2,5,8,7,9,4]
lst2=[3,4,5,6,7,8,9]
union=[]

for i in lst1:
    if i not in union:
        union.append(i)
for j in lst2:
    if j not in union:
        union.append(j)  
print("Union is :",union)              


 