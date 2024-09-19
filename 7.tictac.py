#declare the board
#print the board
#current 
#loop
# Ask the current player for move
from termcolor import colored

X= 'X'
O= "O"

board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]
         ]

def check_value(row):
    if row == X:
        return colored(row,"red")
    return colored(row,"green")
    

def print_board(board): # print the board
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {check_value(row[0])} | {check_value(row[1])} | {check_value(row[2])} ')
        print(line)


def check_winner(board):
    #check rows
    for row in board:
        if (row[0] == row[1]==row[2] != ' '):
            return True
    
     #check columns
    for column in range(3):
        if(board[0][column]== board[1][column] == board[2][column] != " "):
            return True

      #check diagonals
    if(board[0][0]==board[1][1]==board[2][2] != " ") or \
        (board[0][2]==board[1][1]==board[2][0] != " "):
        return True    
    
    return False

#Enter the loop
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_position(prompt):
    while True:
        try:
           position = int(input(prompt))
           if(position<0 or position >2):
                raise ValueError
           return position
        except ValueError:
            print("value must be integer")

def get_move(current_player):
    print(f"Player {current_player}'s turn")
    while True:
        # row = int(input("Enter Row (0-2): "))
        # column = int(input("Enter Column (0-2): "))
        row = get_position("Enter Row (0-2): ")
        column = get_position("Enter Column (0-2): ")
        
        if board[row][column] == " ":
            board[row][column] = current_player;
            break
        print("The spot is already Taken")
            

def main():
    print_board(board)

    current_player = X; #set the current player

    while True:
        get_move(current_player)
        # print(f"Player {current_player}'s turn")
        # row = int(input("Enter Row (0-2): "))
        # column = int(input("Enter Column (0-2): "))
        
        # if board[row][column] == " ":
        #     board[row][column]= current_player;
        # else:
        #     print("The spot is already Taken")
        #     continue
        


        print_board(board)

        if check_winner(board):
            print(f'Player {current_player} wins! ')
            break

        if is_full(board):
            print(f'Board is full')
            break

        # if current_player == X:
        #     current_player == 'O'
        # else:
        #     current_player = "X"

        current_player = O if current_player == X else X



if __name__ == '__main__':
    main()
    

# line = '---+---+---'
# sept = " | "
# box_plot = [
#     [" "," "," "],
#     [" "," "," "],
#     [" "," "," "]

# ]
# print(box_plot)

# x=3
# val = x//2
# print(line)
# count = 1;
# for row in range(1,x+1):
#     count+=1
#     for column in range(1,x+1):
#         print(row,column,sept ,end= "")
#     print("\n")
#     print(line)

# for i in ar:
#     print(i)
# for row in range(1,4):
#     for column in range(1,4):
#         print(str(row)+sept+str(column))
#         # print(line)
