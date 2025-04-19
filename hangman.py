import requests
from random import choice

# Get word list
response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
word_list = response.text.splitlines()

# Choose a random word
random_word = choice(word_list).lower()  # convert to lowercase for simplicity

# Function to generate the blank version
def guess_word_generator(random_word):
    return ["_"] * len(random_word)

# Hangman ASCII stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Game logic
def play_hangman():
    max_tries = len(hangman_stages) - 1
    wrong_guesses = 0
    guessed_letters = set()
    current_guess = guess_word_generator(random_word)

    while wrong_guesses < max_tries and "_" in current_guess:
        print(hangman_stages[wrong_guesses])
        print("Word:", " ".join(current_guess))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in random_word:
            for i, char in enumerate(random_word):
                if char == guess:
                    current_guess[i] = guess
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print("❌ Incorrect!")

    # Final state
    print(hangman_stages[wrong_guesses])
    if "_" not in current_guess:
        print("🎉 You guessed the word:", random_word)
    else:
        print("💀 Game over! The word was:", random_word)

# Run the game
play_hangman()
