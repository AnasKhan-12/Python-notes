import random

def play_game():
    number = random.randint(1, 50)
    while True:
        try:
            user_input = int(input("Enter the guessed number (1-50): "))
            if user_input == number:
                print("Congrats! You guessed the number.")
                break
            elif user_input > number:
                print("Too High")
            else:
                print("Too Low")
        except ValueError:
            print("Enter a valid number.")

while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
