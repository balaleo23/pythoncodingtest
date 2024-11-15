import string
import random

def generate_password(length, include_uppercase, include_numbers, include_special):
    if(length < (include_numbers + include_special + include_uppercase)):
        raise ValueError ('Value must be greater than 3')
    
   
    password = random.choice(string.ascii_lowercase)

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation) 

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters +=  string.punctuation 
    
    for _ in range(length - len(password)):
        password += random.choice(characters)
    
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

    # return password

def main():
    length = int(input("Enter Password Length: "))
    include_uppercase = (input("include uppercase letters? (y/n): ")).lower() == 'y'
    include_numbers = (input("include numbers? (y/n): ")).lower() == 'y'
    include_special = (input("include Special Characters? (y/n): ")).lower() == 'y'
    try:
        password = generate_password(length, include_numbers, include_uppercase, include_special)
        print(password)
    except ValueError as e:
        print(e)


if __name__ == '__main__' :
    main()  