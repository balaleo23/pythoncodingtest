import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

emojies = {ROCK : '🪨', PAPER : '🧻' , SCISSOR: '✂️'}
choices = tuple(emojies.keys())
# choices = ('r','p','s')

def get_user_choice():
    while(True):
        user_choice = input("Rock, Paper, or Scissor? (r/p/s) :").lower()
        if (user_choice in choices):
            return user_choice
        else:   
            print('inavlid choices')
            
def display_choices(user_choice,computer_choice):
    print(f'You Selected {emojies[user_choice]}')
    print(f'Computer Selected {emojies[computer_choice]}')

def play_game():
    while True:
        user_choice =get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice,computer_choice)

        determine_winner(user_choice,computer_choice)

        should_continue = input("continue (y/n): " ).lower()
        if(should_continue =='n'):
                break

def determine_winner(user_choice,computer_choice):
    if(user_choice == computer_choice):
        print('Tie')
    elif(
        (user_choice == ROCK and computer_choice == SCISSOR) or 
        (user_choice ==SCISSOR and computer_choice == PAPER ) or 
        (user_choice ==PAPER and computer_choice == ROCK ) ):
        print('You win')
    else:
        print("computer Won")
        
play_game()    

