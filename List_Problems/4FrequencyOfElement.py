#4.Find the frequency of each element in a list.

# lst=[1,2,1,3,1,4,2,5,7,9,7]
# freq={}
# for i in lst:
#     if i in freq:
#         freq[i]=freq[i]+1
#     else:
#         freq[i]=1
# print(freq)            




lst=[1,2,1,2,1,3,4,3,6,7,1]
freq={}
for i in lst:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)







