# check if ram present in list then print index num of ram

# l = ["kailash", "shivam", "akshay", "ram", "kunal"]

# if "ram" in l:

#     print("ram found at index:", l.index("ram"))

# else:
#     print("ram not found")



####################################################


# lst=["A","kailash","patel","noida","raj"]

# if "patel" in lst:
#     print("item present at index num:",lst.index("patel"))
# else:
#     print("item not present in lst.")    






# lst=["ajay","sandeep","ram","mahes","ram"]
# result=[]
# for x in range(len(lst)):
#     if lst[x]=="ram":
#         result.append(x)
        
# print("ram present at indexes:",result)







lst=["ram","ajay","sandeep","ram","mahesh","ram"]
item="ram"
result=[]
for x in range(len(lst)):
    if lst[x]==item:
        result.append(x)

if not result:
    print("Item not present in lst:")    
else:    
    print("item present at indexes:",result)        

