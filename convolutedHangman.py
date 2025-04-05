"""
This is Moses's hangman game.

These are my modules and functions. Added some comments to explain what each function does.
The hangman() function from the pseudocode was split into a logic function and a main function.
The logic function contains the main game loop and handles the game logic, while the main function is responsible for running the game and displaying the welcome message.
This was done to make life easier for me and to make the code more readable.


Enjoy the ASCII art, courtesy of https://www.asciiart.eu/space/astronauts. 
     _..._
      .'     '.      _
     /    .-""-\   _/ \
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
  jgs    \   `\  \
          `-._/._/
"""
from random import choice
from os import getcwd
from sys import exit


def _loading_words_from_txt():
    ''' This is my attempt to load words from a text file. '''
    try:
        with open("words.txt", "r") as file:
            content = file.read()
            words = [word.strip().upper() for word in content.split() if word.strip()]
            print(f"\nWords loaded successfully from {getcwd()}/words.txt.")
            print(f"Total words loaded: {len(words)}")
            return words
    except FileNotFoundError:
        print(f"\nError 404: Could not find the file 'words.txt' in {getcwd()}.")
        print("Please ensure the file is in the correct directory.")
        return None
    
def _welcome_message():
    print(
        """
        Welcome to Moses's hangman game!

        The rules are as follows, you have 8 chances to guess the word.
        You'll be playing against the computer's determined word, which is
        randomly selected. You have to guess a letter one at a time, with every
        wrong guess losing you a chance (or life). The game ends when you're
        "hanged" or when you guess the word correctly.

        Good luck!

        """
    )

def _word_select(word_list):
    ''' Selects a random word from the provided list. '''
    return choice(word_list).upper()

def _display_word(word, guessed_letters):
    ''' Displays the current state of the word with guessed letters. '''
    return " ".join(letter if letter in guessed_letters else "-" for letter in word) #In hangman, the letters are separated by spaces. The "-" is used to represent unguessed letters.

def _get_unused_letters(guessed_letters):
    ''' Returns a string of unused letters. '''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Using uppercase letters for hangman. Note that the letters are in uppercase.
    return "".join(letter for letter in alphabet if letter not in guessed_letters)

def _player_turn():
    ''' Handles the player's turn, including input validation. '''
    while True:
        guess = input("Guess a letter: ").upper() #Converts to uppercase.
        try:
            if len(guess) !=1 or not guess.isalpha(): #Checks if the guess is correct or not.
                raise ValueError("Please enter a single letter.")
            return guess
        except ValueError:
            print(f"Invalid Input: {guess}. Please enter a single letter.")

def _computer_turn(unused_letters):
    ''' Selects a random letter from the unused letters. '''
    guess = choice(unused_letters) #Using random(), the "computer" would select an unused letter.
    print(f"Computer guesses: {guess}")
    return guess

def _player_name():
    ''' Gets the player's name. '''
    while True:
        name = input("Please enter your first name: ").strip()
        print("" + "-"*30)
        if name:
            return name
        print("Invalid Input: Name cannot be empty.")

def _logic():
    ''' The logic of the game. '''
    player = _player_name()
    print(f"Welcome to Hangman, {player}!")

    while True:
        current_player = choice([player, "Computer"])
        print(f"{current_player} will go first.")
        print("-"*30)

        words = _loading_words_from_txt()
        if not words:
            print("No words found. Please check your 'words.txt' file and try again.")
            exit(1)

        word = _word_select(words)
        guessed_letters = set()
        unused_letters = _get_unused_letters(guessed_letters)
        lives = 8
        game_over = False

        while not game_over and lives > 0:
            print(f"\nWord: {len(word)} letters: {_display_word(word, guessed_letters)}")
            print(f"Unused letters: {unused_letters}")
            print(f"Lives left: {lives}")
            print(f"{current_player}'s turn.")

            match current_player: #Using match-case to determine the current player.
                case current_player if current_player == player:
                    guess = _player_turn()
                case "Computer":
                    guess = _computer_turn(unused_letters)

            if guess in guessed_letters:
                print(f"You have already guessed {guess}. Try again.")
                continue

            guessed_letters.add(guess)
            unused_letters = _get_unused_letters(guessed_letters)

            match guess in word:
                case True: 
                    print(f"Correct guess: {guess}")
                    if all(letter in guessed_letters for letter in word):
                        print(f"Congratulations {current_player}! You guessed the word: {word}.")
                        game_over = True
                case False:
                    print("Wrong guess.")
                    lives -= 1
                    current_player = player if current_player == "Computer" else "Computer"
                    print(f"{current_player}'s turn. Also, you have {lives} lives left.")

        if lives == 0:
            print(f"Game over! The word was: {word}.")

        repeat = input("Do you want to play again? (yes/no): ").strip().lower()
        match repeat:
            case "yes":
                print("Starting a new game...")
                print("-" * 30)
                continue
            case "no":
                print("Thanks for playing Moses's Hangman!")
                print("Goodbye!")
                exit(0)
            case _:
                print("Invalid input. Exiting the game.")
                exit(1)
        print("-" * 30)

"""
Now, the main function that runs the game. This is the cooking part of the game.
Essentially, this is where all the ingredients come together to make the game work.
"""

def _hangman():
    ''' Main function to run the game. '''
    _welcome_message() #My welcome message goes here.
    _logic() #This is where the logic of the game is executed.
_hangman()