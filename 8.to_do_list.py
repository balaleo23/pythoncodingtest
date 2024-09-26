
def add_tasks():
    while True:
        value = str(input("Enter your Tasks: ").strip())
        try:
            if(type(value)!=str or value =="" or value == " "):
                raise ValueError
            return value
            
        except ValueError:
            print("enter proper values")


def getinput(options):
    while True:
        print("ToDo List menu:")
        for option in options:
            print(option)
        try:
            n = int (input("Enter you Choice: "))
            if(n<0 or n>4):
                raise ValueError
            else:
                return n

        except ValueError:
            print("invalid value")
            print("\n")


def display_tasks(tasks):
    try:
        if(len(tasks) != 0):
            for index, task in enumerate(tasks,0):
                print(f'\n{index+1}.{task}')
        else:
            print("\nNo tasks in the list") 

    except ValueError:
         print("\nNo tasks in the list") 


def remove_taks(tasks):
     while True:   
        display_tasks(tasks)
        n = int(input("enter you choice for delete: "))
        try:
            if(n <= len(tasks)):
                tasks.pop(n-1)
                return
            else:
                raise ValueError
        
        except ValueError:  
            print("inavlid choice") 


def main():

    options = ["1.View Tasks",
    "2.Add a Task",
    "3.Remove a Task" ,
    "4.Exit"
    ]

    tasks =[]

    while True:
        n = getinput(options)
        if(n==1):
            display_tasks(tasks)
            
        elif(n==2):
            value = add_tasks()
            tasks.append(value)
           
        elif(n==3):
            remove_taks(tasks)
           
        elif(n==4):
            # print(" call quit function")
            break
        else:
            raise ValueError

if __name__ == '__main__':
    main() 



#prompt for entering the choice
#if view is none 
#display the no task added 
# again dispaly with choice
# add a task without blank and or enter notify "invalid task"
#remove a task display the task with number
# exit the loop to terminate the program










