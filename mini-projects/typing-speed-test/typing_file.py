import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is fun when you practice every day.",
    "Typing speed tests help improve your accuracy.",
    "Consistency is the key to getting better at coding.",
    "Never stop learning and building cool projects."
]

print("Welcome to the Typing Speed Test!")
print("You will be given a sentence to type.")
print("Type it as fast and accurately as you can.\n")

while True:
    sentence = random.choice(sentences)
    print("Type this sentence:")
    print(f"> {sentence}\n")

    input("Press Enter when you're ready to start...")
    print()

    # Start timer
    start_time = time.time()

    # Get user's typed input
    typed = input("Start typing here:\n> ")

    # End timer
    end_time = time.time()
    elapsed_seconds = end_time - start_time

    if elapsed_seconds == 0:
        elapsed_seconds = 0.001

    typed_words = typed.split()
    word_count = len(typed_words)
    minutes = elapsed_seconds / 60
    wpm = word_count / minutes

    expected_words = sentence.split()
    total_words = len(expected_words)
    correct_words = 0

    for i in range(total_words):
        if i < len(typed_words) and typed_words[i] == expected_words[i]:
            correct_words += 1

    accuracy = (correct_words / total_words) * 100

    print("\n--- Results ---")
    print(f"Time taken: {elapsed_seconds:.2f} seconds")
    print(f"Words typed: {word_count}")
    print(f"Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Correct words: {correct_words}/{total_words}\n")

    play_again = input("Do you want to try again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye.")
        break

    print("\n" + "-" * 40 + "\n")
