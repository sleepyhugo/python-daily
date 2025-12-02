sentence = input("Enter a full sentence: ").lower()

word_counts = {}

for word in sentence.split():

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nWord Count:")
print(word_counts)