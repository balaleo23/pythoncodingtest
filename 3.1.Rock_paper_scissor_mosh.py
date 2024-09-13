import random

emojies = {'r' : '🪨', 'p' : '🧻' , 's': '✂️'}
choices = ('r','p','s')

while(True):
    user_choice = input("Rock, Paper, or Scissor? (r/p/s) :").lower()
    if (user_choice not in choices):
        print('inavlid choices')
        continue

    computer_choice = random.choice(choices)

    print(f'You Selected {emojies[user_choice]}')
    print(f'Computer Selected {emojies[computer_choice]}')

    if(user_choice == computer_choice):
        print('Tie')
    elif(
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice =='s' and computer_choice == 'p' ) or 
        (user_choice =='p' and computer_choice == 'r' ) ):
        print('You win')
    else:
        print("computer Won")
        

    should_continue = input("continue (y/n): " ).lower()
    if(should_continue =='n'):
        break

    

