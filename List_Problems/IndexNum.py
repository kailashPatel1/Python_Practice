# 11. find item index num:

# lst=["ram","pawan","visnu","ajay"]
# if "visnu"in lst:
#     print(lst.index("visnu"))
# else:
#     print("not found")    
     


# Find multiple indexes:

lst=["A","B","A","C","A","D"]
item="A"
result=[]

for i in range(len(lst)):

    if lst[i]==item:
        result.append(i)
if result==[]:           #or, len(result)==0:
    print("Item not present in list.")  
    
else:
    print("Item present at index num:",result)          
  


 

    


