#10. Rotate a list by k positions (left or right).

lst = [1, 2, 3, 4, 5]
k = 2
n = len(lst)
k = k % n   
result = []
for i in range(k, n):
    result.append(lst[i])
for i in range(k):
    result.append(lst[i]) 
print(result)


 

# ###############


lst=[5,4,3,2,1]
k=2
n=len(lst)
k=k%n
result=[]
for i in range(k,n):
    result.append(lst[i])
for i in range(k):
    result.append(lst[i]) 
print(result)   

