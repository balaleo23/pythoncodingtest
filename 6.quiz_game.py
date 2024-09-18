from termcolor import colored, cprint
import random 

QUESTION = 'question'
ANSWER = 'Answer'
OPTION ='options'

def ask_question(index, question, option):
        print(f'Question {index}: {question}')
        for option in option:
            print(option)
        return input ('Your ANSWER: ').upper().strip()

def run_quiz(quiz):
    score = 0
    random.shuffle(quiz)

    for index, item in enumerate(quiz,1):
        answer = ask_question(index,item[QUESTION],item[OPTION])

        if answer == item[ANSWER]:
            score +=1
            cprint("Correct", "green")
        else:
            cprint(f'Wrong ,The Correct answer is {items[ANSWER]}',"red")

    print(f'Your Final Score is {score} out of {len(quiz)}')

def main():
    quiz = [
        {QUESTION : 'What is the Captial of France?',
        OPTION : ['A.Berlin','B.Madrid', 'C.Paris', 'D.Rome'],
        ANSWER: 'C'},
        {QUESTION : 'Which planet is known as the red planet?',
        OPTION : ['A.Earth','B.Mars', 'C.Jupiter', 'D.Saturn'],
        ANSWER: 'B'},
        {QUESTION : 'What is the largest ocean on the Earth?',
        OPTION : ['A.Atlantic', 'B.Indian', 'C.Arctic','D.Pacific'],
        ANSWER: 'D'}
    ]
    run_quiz(quiz)

if __name__ == '__main__':
     main()
