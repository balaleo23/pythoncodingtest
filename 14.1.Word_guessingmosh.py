# read the list of wordss
#choose a random word
# attempts = 6
# Loop _attemps >0
# Display word
# For each letter in secret word
# if user guessed that letter 
# print it
# else  
# print the _
# ask the user to enter a letter
# validate input
# single character
# only from A-z
# duplicate 
# if any of these validation failed
# secret word
# good Guess
# check if the word is guessed
# for each letter in secret in the guessed letter
# the word is not guessed
# congrats 
# break
# Else
# print wrong guess
import random
import re

def readwords():
    try:
        with open ("words.txt",'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError as fe:
          print("words.txt does not found")
          return []
    

def displayword(secretword, guessed_letters):
    words_to_display = ''

    for letter in secretword:
        if letter in guessed_letters:
            words_to_display += letter
        else:
            words_to_display += '_'

    print(words_to_display)


def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Enter only one letter")
        elif not re.search('[a-z]',guess):
            print("Enter only letters from a to z.")
        elif guess in guessed_letters:
            print("You already guessed that word")
        else:
            return guess
        
def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

    

def main():
    words = readwords()
    if not words:
        print("No words loaded")
        return
    secret_word = random.choice(words)
    print(secret_word)
    

    attempts = 6
    guessed_letters = []
    while attempts > 0:
        displayword(secret_word, guessed_letters)
        guess = get_guess(guessed_letters)
        if guess in secret_word:
            guessed_letters.append(guess)

        if guess in secret_word:
            print("Good Guess")
            if  is_word_guessed(secret_word, guessed_letters):
                print("Congratulations! You Guessed the word")
                break
        else:
            print("Wrong Guess")
            attempts -= 1
            if attempts == 0:
                print(f"Game over! The word was {secret_word}")
        





if __name__ == '__main__':
    main()