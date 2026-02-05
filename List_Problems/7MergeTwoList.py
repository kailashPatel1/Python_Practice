# Merge two sorted lists into a single sorted list.

lst1 = [1, 6, 5, 7]
lst2 = [2, 12, 6, 8]
# lst1.sort()
# lst2.sort()

i = 0
j = 0
merged = []

while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1

while i < len(lst1):
    merged.append(lst1[i])
    i += 1

while j < len(lst2):
    merged.append(lst2[j])
    j += 1

print(merged)

