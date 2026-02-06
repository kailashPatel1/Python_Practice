#6. Count word frequency in a sentence using dictionary.


n = input("Enter a sentence: ")

freq = {}   

for word in n.split():      # loop over words in the sentence
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

print(freq)   




