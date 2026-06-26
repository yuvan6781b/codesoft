import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_choices(user_choice, computer_choice):
    """Display the choices of the user and the computer."""
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

def main():
    # Initialize scores
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Prompt the user for their choice
        while True:
            user_choice = input("\nChoose rock, paper, or scissors: ").lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                break
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
        
        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Determine the result
        result = determine_winner(user_choice, computer_choice)
        
        # Display the results
        display_choices(user_choice, computer_choice)
        
        if result == 'win':
            print("You win!")
            user_score += 1
        elif result == 'lose':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        # Display scores
        print(f"Score - You: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing! Final scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

if __name__ == "__main__":
    main()
