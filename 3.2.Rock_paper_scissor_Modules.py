import random

emojies = {'r' : '🪨', 'p' : '🧻' , 's': '✂️'}
choices = ('r','p','s')

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
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice =='s' and computer_choice == 'p' ) or 
        (user_choice =='p' and computer_choice == 'r' ) ):
        print('You win')
    else:
        print("computer Won")
        
play_game()    

