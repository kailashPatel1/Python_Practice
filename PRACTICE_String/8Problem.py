# 8. Remove duplicate characters from a string.

# s = input("Enter a string: ")

# result = ""
# for char in s:
#     if char not in result:
#         result += char

# print("After removing duplicates:", result)




# 

# a=input("Enter a string:")
# final=""

# for ch in a:
#    if ch not in final:
#       final=final+ch
# print("after removing duplicate:",final)      



# a=["a","b","c","a","c"]

# result=[]
# for x in a:
#     if x not in result:
#         result.append(x)
# print(result)






 

lst=["a","b","a","c","a"]
result=[]
for x in lst:
    if x not in result:
        result.append(x)
print("After removing duplicates",result)        

