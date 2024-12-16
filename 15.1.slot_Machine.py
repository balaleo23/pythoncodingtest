#Entering the balance which we like to play
#valid it should be digits
# should be positive number
#once the balance amount is set it should be returned
import random

def set_balance():
    while True:
        
        
        try:
            balance = int(input("Enter your Starting balance: $"))
            if balance <= 0 : 
                raise ValueError 
            
            print()
            print("Welcome to Slot Machine Game!")
            print(f'You Start with a balance of ${balance}')

            return balance

        except ValueError as ex:
            print("Please enter a valid number") 


def set_betamount(amount):
    while True:
        try:
            betamount = int(input("Enter your bet amount :$"))

        
            if betamount <=0:
                print(f"Invalid bet amount. you can bet between $1 and ${amount}")
            elif betamount > amount:
                print(f"Invalid bet amount. you can bet between $1 and ${amount}")
            else:
                return betamount
                
        except ValueError as ve:
                print("Please enter valid number for the bet amount")

symbols = ['🍒', '🍋', '🔔', '⭐️', '🍉']

def display_symbol():
    symbol1 = random.choice(symbols)
    symbol2 = random.choice(symbols)
    symbol3 = random.choice(symbols)

    return (symbol1, symbol2, symbol3)

def game_play():
    pass

def main():
    
    newbalance =  set_balance()
    print()
    
    while newbalance:
        print()
        print(f'Current Balance: ${newbalance}')
        betamount = set_betamount(newbalance)
        # print(betamount)
        sym1,sym2 ,sym3 = display_symbol()
        
        print(sym1 + "|" + sym2 + "|" + sym3 )
        if (sym1 == sym2 or sym2 == sym3 or sym3 == sym1 ):
            newbetamount = 2*betamount
            newbalance = newbalance+newbetamount 
            print("you won")   
            print(f'newbalance : ${newbalance}')
        elif(sym1==sym2==sym3):
            newbetamount = 10*betamount
            newbalance = newbalance+newbetamount
            print(f"you won ${newbetamount}")
            print(f'newbalance : ${newbalance}')
        else:
            newbalance = newbalance-betamount
            print("you lost!")
        
        if newbalance>0:
            play = input("Do you want to play again? (y/n): ").lower()
            if play!= "y":
                break
        else:
            print("You are out of money! Game over")
            break


if __name__ == "__main__":
    main()
