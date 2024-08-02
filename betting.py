import random

def coin_flip():
    return random.choice(['heads', 'tails'])

def betting_bot(balance):
    while True:
        print(f"Your current balance: {balance}")
        bet_amount = int(input("Enter your bet amount (0 to quit): "))
        
        if bet_amount == 0:
            print("Exiting the betting bot. Goodbye!")
            break
        
        if bet_amount > balance:
            print("Insufficient balance! Please enter a lower bet amount.")
            continue
        
        guess = input("Enter your guess (heads or tails): ").lower()
        if guess not in ['heads', 'tails']:
            print("Invalid guess! Please enter 'heads' or 'tails'.")
            continue
        
        result = coin_flip()
        print(f"The coin landed on: {result}")
        
        if result == guess:
            print("Congratulations! You won.")
            balance += bet_amount
        else:
            print("Sorry! You lost.")
            balance -= bet_amount
        
        if balance == 0:
            print("You've run out of balance. Exiting the betting bot.")
            break

if __name__ == "__main__":
    initial_balance = 100  # You can set the initial balance here
    betting_bot(initial_balance)
