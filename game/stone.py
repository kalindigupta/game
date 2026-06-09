import random
def decide_winner(user, comp):
    rules = {
        "s": "sc",   
        "p": "s",    
        "sc": "p"    
    }

    if user == comp:
        return "draw"
    elif rules[user] == comp:
        return "user"
    else:
        return "computer"


def play():
    choices = {"s": "Stone", "p": "Paper", "sc": "Scissors"}

    user = input("Choose (s = Stone, p = Paper, sc = Scissors): ").lower()

    if user not in choices:
        print("❌ Invalid input")
        return None

    comp = random.choice(list(choices.keys()))

    print(f"You: {choices[user]}")
    print(f"Computer: {choices[comp]}")

    return decide_winner(user, comp)
user_score = 0
comp_score = 0
streak = 0

while True:
    print("\n===== GAME MENU =====")
    print("1. Play")
    print("2. Show Score")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = play()

        if result == "user":
            print("🔥 You win!")
            user_score += 1
            streak += 1

        elif result == "computer":
            print("💻 Computer wins!")
            comp_score += 1
            streak = 0

        elif result == "draw":
            print("🤝 Draw!")
            streak = 0

    elif choice == "2":
        print(f"\nScore → You: {user_score} | Computer: {comp_score}")
        print(f"🔥 Current Winning Streak: {streak}")

    elif choice == "3":
        print("Exiting game... 👋")
        break

    else:
        print("❌ Invalid choice")