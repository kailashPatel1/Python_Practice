# 2.Sort a dictionary by key or value

# d = {"b": 20, "a": 10  , "d": 40, "c": 30}  

# key = dict (sorted(d.items()))   
# print(key) 






# dic={"c":2,"d":5,"a":8}
# key=dict(sorted(dic.items()))
# print(key)







lst=[2,4,5,18,12,8]

maxi=lst[0]
mini=lst[0]

for x in lst:
    if x>maxi: 
        maxi=x
    if x<mini:
        mini=x
print(f"maximun num is:{maxi} ") 
print(f"minimum num is:{mini} ") 




