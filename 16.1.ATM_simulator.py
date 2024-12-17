# welcome message with option
# display message to choose the option


def display_message():
    while True:
        try:
            print('\n Welcome to the ATM!')
            print("1. Check Balance")
            print("2. Deposit")
            print("3. WithDraw")
            print("4. Exit")
            value = int(input ("Please Choose an option: "))
            if value > 4:
                raise ValueError
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print("Enter valid option")

def check_balance(amt):
    print(f"\nyour current balance is ${amt}")

def deposit():
    while True:
        try:
            amount = int(input("enter the amount to be deposit: $"))
            if amount <= 0:
                print("Deposit amount must be positive")
            return amount
        except ValueError:
            print("Please enter the valid number")


def withdraw(current_amount):
    while True:
        try:
            withdraw_amount = int(input("enter the amount to be withdraw: $"))
            if withdraw_amount <= 0 :
                raise ValueError
            elif withdraw_amount>current_amount:
                print("Insufficient funds")
                continue
            return withdraw_amount
        except ValueError:
            print("Please enter the valid number")

def main():
    current_amount = 0 
    while True:
        option = display_message()
        
        if option == 1:
            check_balance(current_amount)
            
        if option ==2:
            amount = deposit()
            current_amount += amount
            print(f"Sucessfully deposited ${amount}")
        if option ==3:
            if current_amount>0:
                amount = withdraw(current_amount)
                current_amount -= amount
                print(f"Sucessfully withdrew ${amount}")
            else:
                print("Insufficient funds, Please deposit fund for further transaction")
        if option ==4:
            print(" Transaction Completed")
            break



        
        

if __name__ == "__main__":
    main()

    
    
        
    
