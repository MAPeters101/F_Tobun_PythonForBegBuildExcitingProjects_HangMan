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