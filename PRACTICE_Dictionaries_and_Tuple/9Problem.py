#  Combine two dictionaries and sum values of common keys.


d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

result = d1.copy()   # start with d1

for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
 
print(result)


 


  