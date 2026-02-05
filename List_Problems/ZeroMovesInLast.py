#8.Move all zero elements to the end of a list.

lst=[0,3,0,5,10,0,6]
pos=0 
for i in range(len(lst)):
    if lst[i] !=0:
        lst[pos]=lst[i]
        pos=pos+1
while pos < len(lst):
    lst[pos]=0
    pos=pos+1
print(lst)


