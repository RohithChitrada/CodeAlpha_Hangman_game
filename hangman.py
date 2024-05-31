import random

def choose_word():
    words = ["python", "hangman", "java", "programming", "leetcode", "computer", "algorithm", "function"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print(f"You have {tries} tries left.")
        print("Used letters: ", ' '.join(used_letters))
        print("This is a ",len(word)," letter word.")        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        
        user_letter = input("Guess a letter: ").lower()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                tries -= 1
                print(f"\nYour letter, {user_letter}, is not in the word.")
        
        elif user_letter in used_letters:
            print("\nYou have already used that letter. Guess another letter.")
        
        else:
            print("\nInvalid character. Please try again.")

    if tries == 0:
        print(display_hangman(tries))
        print(f"Sorry, you lost. The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word}!")

hangman()