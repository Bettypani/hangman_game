# Hangman Game

## Overview
This is the Hangman game implemented in Python. The player attempts to guess a randomly chosen word by suggesting letters within a certain number of guesses.

## Features
- Random word selection from a predefined list.
- User-friendly interface displaying the current word and letters guessed.
- Visual representation of the hangman that updates with each incorrect guess.
- Option to play again after the game ends.

## Requirements
- Python 3.x
- External files: `hangman_words.py` (contains the word list) and `hangman_art.py` (contains the hangman stages and logo).

## How to Play
1. Run the script.
2. A random word will be chosen, and you will see underscores representing each letter in the word.
3. Guess letters one at a time.
4. If the guessed letter is in the word, it will be revealed in the appropriate positions.
5. If the guessed letter is not in the word, you will lose a life.
6. The game ends when you either guess the word or run out of lives.
7. You will be given the option to play again.

## Instructions to Run
1. Ensure you have Python installed on your machine.
2. Make sure to have the `hangman_words.py` and `hangman_art.py` files in the same directory.
3. Run the script in your terminal or command prompt:
   ```bash
   python hangman.py
