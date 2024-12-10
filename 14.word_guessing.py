# list of the words to be guessed
# choose the random words
# then we should loop the length of the word print it witht the _
# validate the words with numbers and multiple letters
# replace the hypen with the occurence of the word
# allow six wrong guesses
# reveal the word if word the is right

import random


words = ["python", "Astronaut","Polymorphism"]


def main():
    random.shuffle(words)
    newword = words[0]
    print(newword)
    empty = ""
    for i in range(1, len(newword)):
        empty += "".join("_")

    print(empty)
    wrong_guess = 0

    while wrong_guess< 6:
        guess_letter = (input("Guess the letter: "))

        try:
            if len(guess_letter) > 1 :
                print("Enter the only one letter")  
            elif (guess_letter.isnumeric()):
                raise ValueError
            elif(guess_letter.isalpha()):
                if(guess_letter in (newword)):
                    if (guess_letter not in empty):
                        for i in range(0, len(newword)):
                            if (guess_letter.lower() == newword[i].lower()):
                                empty = empty[:i] + guess_letter + empty[i+1:]
                        print(empty)
                    else:
                        print("letter already found")     
                else:
                    print("letter not found")
                    wrong_guess += 1
                if(empty == newword):
                        print("Won")
                        break  
            else:
                raise ValueError

            
        except TypeError as T :
                print ("TypeError :Enter only letters")
                wrong_guess += 1
        except ValueError as V :
                print ("ValueError: Enter only letters")
                wrong_guess += 1



if __name__ == '__main__' :
    main()  
