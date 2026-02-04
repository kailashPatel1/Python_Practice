# 5. Find common elements between two lists

# lst1=[1,3,4,6,7,9,2]
# lst2=[3,8,10,4,7]        

# common=[]      
# for x in lst1:

#     if x in lst2 and x not in common: 
       
#         common.append(x)
# print("common elements",common)

 




 
l1=[2,3,5,8,4]
l2=[7,2,5,4,9,12]
common=[]
for k in l1:
    if k in l2 and k not in common:
        common.append(k)
print("Common itemes:",common)

