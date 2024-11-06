#first generating the secret number
#prompt to guess the number
# finding the bulls and cows bulls are actual wrong digits and location
# cows are right digits and the location
# finally if there is 0 cows and 4 bulls 
# player won

import random

def has_doubles(n):
    return len(set(str(n))) < len(str(n))

def check_position(guessvalue,placements):
    cows = 0
    bulls = 0
    # print(guessvalue)
    print(placements)
    for i,j in zip(guessvalue, placements):
            if (i ==j):
                bulls += 1 
            elif(i in placements):
                cows += 1
                    

    print(f"cows {cows} and bulls {bulls}")
    if(bulls==4):
        return True
    


def guess(placements):
    while True:
        try:
            guessvalue =  int(input("Guess? :"))
            guesslist =[]
            for i in str(guessvalue):
                guesslist.append(int(i))
            if(len(guesslist)>5 or (len(guesslist)<4) or has_doubles(guessvalue) ):
                raise ValueError
            
            get = check_position(guesslist,placements)
            if(get):
                print(F"Congratulations! you Guessed the correct number")
                break
    
            

        except ValueError:
            print("invalid Guess! Please enter a four digit unique value")


def main():
    print("I have generated  a 4-digits number with unique digits. Try to guess it!")
    
    placements = []
    while len(placements) <4:
        generated_number = random.randint(1,9)
        if generated_number not in placements:
            placements.append(generated_number)
    
    guess_value = guess(placements)
    # # generated_number = random.randint(1000, 9999) # need to print it using unique digt
    # # placements = []
    # # print(generated_number)
    # # for i in str(generated_number):
    # #    if i not in placements:
    # #      placements.append(int(i))
    # guess_value = guess(placements)


    

if __name__ == '__main__':
    main()
