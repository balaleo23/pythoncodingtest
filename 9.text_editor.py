 
import os.path

def write_text(file_name):
    print("Enter the text (type SAVE on a new line to save and exit): ")
    while True:
        text= input()
        if text == "SAVE" or text == "save":
           return
        file_name.write(text+'\n') 

def main():
    file_name = input("Enter the Filename to open or create: ").strip()
    if (os.path.isfile(file_name)):
        with open(f"{file_name}", "a") as file_name:
            write_text(file_name)
        # print("file already exisits")
        
    else:  
        try:
            with open(f"{file_name}", "w") as file_name:
                write_text(file_name)
                    # file_name.write("Your text goes here")
        except (FileNotFoundError,OSError):
            print("File could not be opened") 
    

if __name__ == '__main__':
    main() 


#getting the file name avoid the \ in the filename

#getting text as input if the text is SAVE then end the loop 
#file saved
# if the file name exists add the text again