import random
import hangman_words
import hangman_art

def play_game():
    # Load the word list and stages from the imported modules
    word_list = hangman_words.word_list
    stages = hangman_art.stages
    lives = 6  # Number of lives the player has

    # Print the logo at the start of the game
    print(hangman_art.logo)

    # Randomly select a word from the word list
    chosen_word = random.choice(word_list)

    # Create a placeholder for the word with underscores
    display = "_" * len(chosen_word)
    print("Word to guess: " + " ".join(display))

    game_over = False
    correct_letters = []  # List to track correctly guessed letters
    letters_guessed = []  # List to track all guessed letters

    while not game_over:
        # Display the number of lives left
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        guess = input("Guess a letter: ").lower()  # Get user input
        letters_guessed.append(guess)  # Add guess to the list of guessed letters
        print(f"The letters you guessed are {letters_guessed}")

        # Check if the user has already guessed the letter
        if guess in correct_letters or guess in letters_guessed[:-1]:
            print(f'You already guessed {guess}')
            continue

        # Update the display based on the guess
        display = ""
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)  # Add to correct letters
            else:
                display += "_" if letter not in correct_letters else letter

        print("Word to guess: " + " ".join(display))

        # Check if the guessed letter is in the chosen word
        if guess not in chosen_word:
            lives -= 1  # Lose a life
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            if lives == 0:
                game_over = True
                print(f"***********************The correct word was {chosen_word}**********************")
                print(f"***********************YOU LOSE**********************")
                print('\n' * 5)

        # Check for win condition
        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        # Print the current hangman stage
        print(stages[lives])

# Main game loop
while True:
    play_game()
    play_again = input("Would you like to play again yes or no \n").lower()

    if play_again != 'yes':
        print("Thank you for playing!")
        break
