import random

actual_number = random.randint(1,100)

while(True):
    number_guess = int ( input ("Guess the number: between 1 and 100: "))


    try:
        if(number_guess<actual_number):
            print('Your Guess is very low')

        elif(number_guess>actual_number):
            print('Your Guess is high Try Again')

        else:
            print("congratz!!")
            break

    except ValueError:
        print("invalid input")




    