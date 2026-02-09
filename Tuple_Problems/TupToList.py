##2.How do you convert a tuple into a list and then modify it?

tup=(2,4,6,8)
lst=list(tup)
lst.append(15)
lst[2]=20
print("Tuple to list:",lst)

t=tuple(lst)

print("List to tuple:",t)


