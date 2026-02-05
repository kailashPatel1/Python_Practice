# Remove duplicate elements from a list while preserving order.


lst=[2,3,2,5,4,5,2]

result=[]
for i in lst:
    if i not in result:
        result.append(i)
print(f"After removing duplicates:{result}")
        