
import random


def rolldie():
    return random.randint(1,6)

def playturn(player_name):
    turn_score = 0
    
    print(f"\n{player_name}'s turn")
    
    while True:
        roll = rolldie()
        print(f"you Rolled a {roll}")
        if (roll ==1 ):
            return 0
        turn_score = turn_score + roll
        choice = input('Roll again? (y/n): ').lower()
        if (choice != 'y'):
            return turn_score

        

def main():
    scores = [0,0]
    current_player = 0

    while True:
        player_name = f'player {current_player +1 }'
        turn_score = playturn(player_name)
        scores[current_player]  += turn_score

        print(f'\n you scored {turn_score} points this turn')
        print(f'Current score Player 1: {scores[0]}, Player 2: {scores[1]}')

        if(scores[current_player]>=100):
            print(f'{player_name} wins!')
            break
        
        current_player = 1 if current_player == 0 else 0







if __name__ == '__main__':
    main()


#run the until the player wins infinite loops to start with
#player 1 takes a turn
# Roll a die
# if roll == 1
#   turn point = 0
# turn ends
# else 
# add roll to the turn points
# ask the user if they want to repeat
#if yes repeat
#else turn ends
#
# update player 1 points
# print statistics
# check if player score greater than 100
#player wins
# else continue

