#1. How do you remove duplicate elements from a list using a set?

# s=[1,2,3,2,4,3,2,5,3]

# result=set()
# for i in s:
#     if i not in result:
#         result.add(i)
# print(result)




#####################

lst=[1,1,2,3,3,5,4]
result=set()
for i  in lst:
    if i not in result:
        result.add(i)
print(result)


