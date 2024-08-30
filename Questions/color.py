import random

def color_prediction_game():
    colors = ['red', 'green']
    correct_guesses = 0
    total_rounds = 15  # You can change this to any number of rounds

    print("Welcome to the Color Prediction Game!")
    print("Guess whether the color is 'red' or 'green'.")

    for round_number in range(1, total_rounds + 1):
        print(f"\nRound {round_number}")
        chosen_color = random.choice(colors)
        
        guess = input("Enter your guess: ").strip().lower()
        
        if guess not in colors:
            print("Invalid input! Please enter 'red' or 'green'.")
            continue
        
        if guess == chosen_color:
            print("Correct!")
            correct_guesses += 1
        else:
            print(f"Wrong! The correct color was {chosen_color}.")

    print("\nGame Over!")
    print(f"You guessed correctly {correct_guesses} out of {total_rounds} rounds.")

# Run the game
color_prediction_game()