import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("--------------------------------------")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Validate range
            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.\n")
                continue

            # Compare guess with actual number
            if guess < number_to_guess:
                print("📉 Too low! Try again.\n")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly.")
                print(f"🏆 It took you {attempts} attempts to guess the right number.")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.\n")

def main():
    while True:
        number_guessing_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! See you next time.")
            break
        print("\n-----------------------------\n")

if __name__ == "__main__":
    main()
