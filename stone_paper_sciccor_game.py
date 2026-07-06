import random

def get_winner(comp, user):
    """Returns True if User wins, False if Computer wins, None if Tie."""
    if comp == user:
        return None
        
    winning_rules = {
        'r': 's',  # Rock beats Scissor
        'p': 'r',  # Paper beats Rock
        's': 'p'   # Scissor beats Paper
    }
    
    if winning_rules[user] == comp:
        return True
    return False

user_score = 0
comp_score = 0
total_matches = 0

print("=== Welcome to Rock, Paper, Scissors Game! ===")
print("Type 'x' anytime to exit the game.")

while True:
    print(f"\n--- Round {total_matches + 1} ---")
    
    choices = ['r', 'p', 's']
    comp = random.choice(choices)

    user = input("Enter r (Rock), p (Paper), s (Scissor), or x (Exit): ").lower()

    # Exit option
    if user == 'x':
        print("\n==========================================")
        print(" FINAL GAME STATS:")
        print(f"Total Matches Played: {total_matches}")
        print(f"Your Wins: {user_score}")
        print(f"Computer Wins: {comp_score}")
        print(f"Ties: {total_matches - (user_score + comp_score)}")
        print("==========================================")
        print("Thank you for playing!  ")
        break

    if user in choices:
        total_matches += 1
        result = get_winner(comp, user)
        
        print(f"Computer chose: {comp.upper()}")
        print(f"You chose: {user.upper()}")

        if result is None:
            print(" It's a Tie!")
        elif result is True:
            print(" You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            comp_score += 1
    else:
        print(" Invalid input! Please enter only r, p, s, or x.")
