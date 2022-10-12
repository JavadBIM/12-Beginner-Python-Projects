import random
from words import words
import string


def get_valid_words(words):
    word = random.choice(words)  # randomly choose a word
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


lives = 6


def hangman():
    global lives
    word = get_valid_words(words)  # letters in the word
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # getting user inputs
    while len(word_letters) > 0 and lives > 0:
        # letters you have used
        print("you have", lives, "lives left" ", You Have used these letters", " ".join(used_letters))
        # what is the current words
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current Word", " ".join(word_list))

        user_letter = input("Guess a Letter : ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is wrong")

        elif user_letter in used_letters:
            print("You have already guessed this character")

        else:
            print("Invalid Character")
    if lives == 0:
        print("you have died sorry")
    else:
        print(f"you guessed the right word : {word}")


hangman()
