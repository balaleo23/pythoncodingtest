a = input("Roll the Dice? Y/N ")


def rolling():
    if a.lower() == "y":
        
        print("Rolling the dice...")
        from random import randint
        print("The value is....")
        print(randint(1,6))
    elif a.lower() == "n":
        print("Thanks for playing")
        exit()   
    else:   
        print("Invalid input")

while True:
    rolling()
    a = input("Roll the Dice? Y/N ")
   



