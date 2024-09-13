# storing variables for input
# computer guess
#if guess R > computer chose P
#computer won
#if guess p and computer chose scissor
# computer won
# if guess r and computer chose scissor
# you won
#loop continue (y/n)
import random

def check_value(value):
    if value not in ('r', 's', 'p'):
        raise ValueError(f"Invalid value:. The value must be 'r', 's', or 'p'.")
    return value
# Example usage

def select_random_value():
    values = ['r', 's', 'p']  # List of values
    return random.choice(values)

# Example usage
rn = select_random_value()
# print(f"Selected value: {random_value}")
while(True):
    n = str(input("Rock , paper , scissors? (r/p/s): "))

    print(n ,"value selected")
    print(rn,"Value genearted")

    if(n == 'r' and rn == 'p'):
        print("Computer won")
        
    if(n =='p' and rn == 's'):
        print("computer won")
        
    if(n=='s'and rn =='r'):
        print("compter won")
        
    else:
        print("you won")
    
        


    try:
        check_value(n)  # This will raise a ValueError    

    except ValueError as e:
        print(e)

        