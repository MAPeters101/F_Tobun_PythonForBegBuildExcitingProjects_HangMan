import random

word_list = ["python", "hangman", "programming", "computer", "algorithm", "software", "bethmedia", "furmilayo"]

chosen_word = random.choice(word_list)

guesses = []
max_attempts = 6
attempts = 0

hangman_stages = [
    """
    -----
    |   |
        |
        |
        |
        |    
    """,
    """
    -----
    |   |
    O   |
        |
        |
        |    
    """,
    """
    -----
    |   |
    O   |
    |   |
        |
        |    
    """,
    """
    -----
    |   |
    O   |
   /|   |
        |
        |    
    """,
    """
    -----
    |   |
    O   |
   /|\  |
   /    |
        |    
    """,
    """
    -----
    |   |
    O   |
   /|\  |
   / \  |
        |    
    """
]


while True:
    print(hangman_stages[attempts])
    display_word = ''
    for letter in chosen_word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(f"Word: {display_word}")

    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses.append(guess)

    if guess in chosen_word:
        print("Correct!")
    else:
        print("Wrong guess!")
        attempts += 1

    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {chosen_word}")
        break
    elif attempts >= max_attempts:
        print(f"Sorry, you ran out of attempts. The word was: {chosen_word}")
        break