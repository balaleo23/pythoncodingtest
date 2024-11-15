# generate string
#ask for length to generate
# need to include the uppercase letter
#include  the numbers
#include special character
import random
import string


def generateword(length,include_uppercase, include_numbers, include_special):
            format = "string.ascii_lowercase "
            if(include_uppercase == 'y'):
                format = format + "+ string.ascii_uppercase "
            if(include_numbers=="y"):
                  format = format+ "+ string.digits"
            if(include_special == 'y'):
                  format = format + '+ string.punctuation'
            
            print(format)
            res = ''.join(random.choices(format, k= length))
            # res = ''.join(random.choices(string.ascii_lowercase  , k=length))
            return res
    
          

def main ():

    length =  int(input("Enter Password Length: "))
    include_uppercase = str (input("Include upperCase letter?(y/n): "))
    include_numbers = str( input("Include numbers?(y/n): "))
    include_special = str(input("Include Special Characters? (y/n): "))

    word_generated = generateword(length, include_uppercase, include_numbers, include_special)
    print(word_generated)
if __name__ == '__main__':
    main()