import random

def play_game():
    print("Welcome to the Number Guessing Game")
    print("The system has selected a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Invalid input. Please enter a numeric value.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Correct guess. You found the number in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for playing.")
            break

main()
