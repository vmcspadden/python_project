import random
import string
from words import words

def get_word(words):
    word = random.choice(words)
    word = word.upper()
    while '-' in word or ' ' in word: 
        word = random.choice(words)
        word = word.upper()

    return word

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word')
        
        elif user_letter in used_letters:
            print('You have already guessed that letter. Please try again')
        
        else: 
            print('Invalid character. Please try again')

    print('Word was', word)

hangman()



