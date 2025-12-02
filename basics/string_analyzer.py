sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"
space_count = 0
letter_count = 0
count = 0

for letter in sentence:
    if letter in vowels:
        count += 1
    if letter ==  " ":
        space_count += 1
    if letter.isalpha():
        letter_count += 1

print("Vowels: ", count)
print("Spaces: ", space_count)
print("Letters: (no spaces):", letter_count)