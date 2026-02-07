#17. Reverse a String Using a Loop

# s=input("Enter astring:")
# rev=""
# for x in s:
#     rev=x+rev
# print("Reversed string:",rev)




# reverse words in a string,
s = input("Enter string:")
a=" ".join(s.split()[::-1])
print(a)




