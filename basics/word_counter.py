sentence = input("Enter a sentence: ")

words = sentence.split()
no_space_sentence = sentence.replace(" ", "")
characters = len(no_space_sentence)

print(f"Words: {len(words)}")
print(f"Characters (no spaces): {characters}")
