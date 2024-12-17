class bank:

    def __init__(self):
        self.current_amount =0
        
        while True:
            option = self.display_message()
            
            if option == 1:
                self.check_balance()

            if option ==2:
                amount = self.deposit()
                self.current_amount += amount
                print(f"Sucessfully deposited ${amount}")

            if option ==3:
                if self.current_amount>0:
                    amount = self.withdraw()
                    self.current_amount -= amount
                    print(f"Sucessfully withdrew ${amount}")
                else:
                    print("Insufficient funds, Please deposit fund for further transaction")
            if option ==4:
                print(" Transaction Completed")
                break

    def display_message(self):
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


    def check_balance(self):
        amount = self.current_amount
        print(f"\nyour current balance is ${amount}")

    def deposit(self):
        while True:
            try:
                amount = int(input("enter the amount to be deposit: $"))
                if amount <= 0:
                    print("Deposit amount must be positive")
                return amount
            except ValueError:
                print("Please enter the valid number")


    def withdraw(self):
        while True:
            try:
                withdraw_amount = int(input("enter the amount to be withdraw: $"))
                if withdraw_amount <= 0 :
                    raise ValueError
                elif withdraw_amount>self.current_amount:
                    print("Insufficient funds")
                    continue
                return withdraw_amount
            except ValueError:
                print("Please enter the valid number")
    

bank1 = bank()
# bank1.main()