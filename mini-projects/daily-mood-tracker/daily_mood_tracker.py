from datetime import date
from collections import Counter
import os


LOG_FILE = "mood_log.txt"


def print_menu():
    print("\n=== Daily Mood Tracker ===")
    print("1. Log today's mood")
    print("2. View mood stats")
    print("3. Exit")


def log_mood():
    mood = input("How are you feeling today? (e.g., happy, tired, stressed): ").strip()

    # Normalize mood to lowercase for consistent stats
    mood = mood.lower()

    if not mood:
        print("Mood cannot be empty. Try again.")
        return

    rating_input = input("On a scale of 1-5, how strong is this feeling? (press Enter to skip): ").strip()

    rating = ""
    if rating_input:
        try:
            rating_value = int(rating_input)
            if 1 <= rating_value <= 5:
                rating = str(rating_value)
            else:
                print("Rating must be between 1 and 5. Rating will be skipped.")
        except ValueError:
            print("Invalid rating. Rating will be skipped.")

    today_str = str(date.today())  # e.g., "2025-12-09"

    # Build line to save: date, mood, (optional) rating
    if rating:
        line = f"{today_str}, {mood}, {rating}\n"
    else:
        line = f"{today_str}, {mood}\n"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(line)
        print("Mood saved!")
    except OSError as e:
        print(f"Error writing to log file: {e}")


def load_entries():
    if not os.path.exists(LOG_FILE):
        return []

    entries = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = [part.strip() for part in line.split(",")]

                if len(parts) == 2:
                    entry_date, mood = parts
                    rating = None
                elif len(parts) == 3:
                    entry_date, mood, rating_str = parts
                    try:
                        rating = int(rating_str)
                    except ValueError:
                        rating = None
                else:
                    # Skip malformed lines
                    continue

                entries.append(
                    {
                        "date": entry_date,
                        "mood": mood,
                        "rating": rating,
                    }
                )
    except OSError as e:
        print(f"Error reading log file: {e}")
        return []

    return entries


def show_stats():
    entries = load_entries()

    if not entries:
        print("No moods logged yet. Try logging one first!")
        return

    print("\n=== Mood Stats ===")
    total_entries = len(entries)
    print(f"Total days logged: {total_entries}")

    # Count moods
    moods = [entry["mood"] for entry in entries]
    mood_counts = Counter(moods)
    most_common_mood, count = mood_counts.most_common(1)[0]
    print(f"Most common mood: {most_common_mood} ({count} times)")

    # Show last 5 entries
    print("\nLast 5 moods:")
    print("-" * 30)
    for entry in entries[-5:]:
        date_str = entry["date"]
        mood = entry["mood"]
        rating = entry["rating"]

        if rating is not None:
            print(f"{date_str} - {mood} (rating: {rating}/5)")
        else:
            print(f"{date_str} - {mood}")


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            log_mood()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
