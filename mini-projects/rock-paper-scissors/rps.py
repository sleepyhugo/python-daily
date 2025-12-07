import random

moves = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

ai_points = 0
player_points = 0

while True:
    player_move = input("Rock, Paper or Scissors? Type 'q' to quit anytime: ").lower()

    # Quit option
    if player_move == "q":
        break

    # Invalid input
    if player_move not in moves:
        print("Invalid answer. Try again!\n")
        continue

    # AI move
    ai_move = random.choice(moves)
    print(f"\nYou chose: {player_move}")
    print(f"The AI chose: {ai_move}")

    # Tie
    if player_move == ai_move:
        print(f"It's a tie! You both chose {player_move}.\n")
        print(f"Score You: {player_points} | AI: {ai_points}\n")
        continue

    # Player wins
    if (
        (player_move == "rock" and ai_move == "scissors") or
        (player_move == "paper" and ai_move == "rock") or
        (player_move == "scissors" and ai_move == "paper")
    ):
        print("You win this round!")
        player_points += 1
    else:
        print("AI wins this round!")
        ai_points += 1

    print(f"Score -> You: {player_points} | AI: {ai_points}\n")

print("\nFinal results:")
print(f"Player Score: {player_points} | AI Score: {ai_points}")

if ai_points > player_points:
    print("Overall winner: AI")
elif ai_points < player_points:
    print("Overall winner: YOU")
else:
    print("Overall result: It's a tie!")
