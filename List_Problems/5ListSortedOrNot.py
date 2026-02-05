# Check whether a list is sorted or not.

lst=[1,2,3,4,5,6,7]

is_sorted=True 
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        is_sorted=False
        break
print(is_sorted)




