import re

def main():
    capital_regex= "[a-z]."
    captial_numeric_regex = "^(?=.*[a-z])(?=." +"*[A-Z])(?=.*\\d)" 
    special_character_regex= ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")

    capital_search = re.compile(capital_regex)
    captial_numeric_search = re.compile(captial_numeric_regex)
    special_character_search = re.compile(special_character_regex)

    password = input ("Enter a password: ")
    print(password)
    strength =0 
    if len(password)<= 4 :
        strength =0 
    if(len(password)>4 and re.search(capital_search,password)) :
        strength = 1
    if(len(password)>4 and re.search(captial_numeric_search,password)) :
        strength = 2  
    if(len(password)>4 and re.search(special_character_search,password)) :
        strength = 3
    print(strength)

if __name__ == '__main__':
    main()
