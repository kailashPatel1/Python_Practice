# 8. Create a function that returns count of vowels in a sentence

def vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# Example
s = input("Enter a sentence: ")
print("Number of vowels:", vowels(s))


  
