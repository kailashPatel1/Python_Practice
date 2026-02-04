# 2. Find maximum and minimum without using built-in functions.

# numbers = [12, 5, 9, 25, 1, 18]

# # Assume first element is max and min
# max = numbers[0]
# min = numbers[0]

# for k in numbers:
#     if k > max:
#         max = k
#     if k < min:
#         min = k

# print("Maximum =", max)
# print("Minimum =", min)

    

###############################   assume 1st items is max and min:

n=[5,10,3,22,7,54,90,33,12]

max=n[0]
min=n[0]

for x in n:
    if x>max:
        max=x
    elif x<min:
        min=x
print("Max num:",max) 
print("min num:",min)           

