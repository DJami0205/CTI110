import random  # Importing the random library to choose a word randomly

# Function to return a dictionary with game data
def get_game_data():
    return {"word_list": ["love", "smile", "beautiful", "be nice", "genuine"], "attempts": 10}

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

# Function to play the Hangman game
def play_hangman():
    game_data = get_game_data()
    word_to_guess = random.choice(game_data["word_list"])  # Choose a random word
    guessed_letters = set()
    attempts_left = game_data["attempts"]

    print("Welcome to Hangman! 🎉")
    
    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")
        print("Current word: ", display_word(word_to_guess, guessed_letters))
        
        guess = input("Guess a letter: ").lower()  # Get user's guess
        
        if guess in guessed_letters:
            print("You already guessed that letter! 🛑")
        elif guess in word_to_guess:
            print("Good guess! 👍")
            guessed_letters.add(guess)
            if set(word_to_guess) <= guessed_letters:  # Check if all letters are guessed
                print("Congratulations! You've guessed the word:", word_to_guess, "🎊")
                break
        else:
            print("Sorry, that's incorrect. ❌")
            guessed_letters.add(guess)
            attempts_left -= 1
        
    if attempts_left == 0:
        print("Game Over! The word was:", word_to_guess, "😞")

# Main function to start the game
def main():
    while True:  # Loop to allow the game to restart
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":  # Check if the user wants to continue
            print("Thanks for playing! 👋")
            break

# Starting the game by calling main()
if __name__ == "__main__":
    main()  # Start the game
