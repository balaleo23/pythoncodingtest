
import re

def check_strength(password):
    strength =0
    
    if(len(password)>=8):
        strength += 1
    if (re.search('[a-z]',password)):
        strength += 1
    if(re.search('[A-Z]',password)):
        strength += 1
    if(re.search('[0-9]',password)):
        strength += 1
    if(re.search('[@#$%^&*!_=+]', password)):
        strength +=1
    return strength


def main():
    password = input("Enter you password: ")
    strength = check_strength(password)
    # print(strength)

    if (strength ==5 ):
        print("your Password is very strong")
    elif (strength ==4 ):
        print("your Password is  strong")
    elif (strength ==3 ):
        print("your Password is  Medium")
    elif (strength ==2):
        print("your Password is  weak")
    else:
        print("your Password is very weak")

if __name__ == '__main__':
    main()
