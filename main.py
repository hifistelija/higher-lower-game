from game_data import data
import art
import random
from replit import clear


#compare user answer
def compare(a, b, guess):
    """Compare the follower counts of personalities A and B based on user guess."""
    if a["follower_count"] > b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(art.logo)
    user_score = 0
    end_game = False
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    
    while not end_game: 
        
        choice_a = choice_b
        choice_b = random.choice(data)
        # Make sure the two personalities are not the same
        while choice_b == choice_a:
            choice_b = random.choice(data)
        
        print(f"Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}")
        print(art.vs)
        print(f"Compare B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}")
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        clear()
        print(art.logo)
        if compare(choice_a, choice_b, user_guess):
            user_score += 1
            print(f"You're right! Current score: {user_score}.")
        else:
            print(f"Sorry, that's wrong. Final score {user_score}")
            end_game = True


game()