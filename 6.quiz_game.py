import sys
from termcolor import colored, cprint
import random 

quiz = [
    {"question" : 'What is the Captial of France?',
     'options' : ['A.Berlin','B.Madrid', 'C.Paris', 'D.Rome'],
     'Answer': 'C'},
     {"question" : 'Which planet is known as the red planet?',
     'options' : ['A.Earth','B.Mars', 'C.Jupiter', 'D.Saturn'],
     'Answer': 'B'},
     {"question" : 'What is the largest ocean on the Earth?',
     'options' : ['A.Atlantic', 'B.Indian', 'C.Arctic','D.Pacific'],
     'Answer': 'D'}
]

score = 0
random.shuffle(quiz)
for index , items in enumerate(quiz,1):
    print(f'Question {index}: {items['question']}')
    for option in items['options']:
        print(option)
    answer = input ('Your Answer: ').upper().strip()
    if answer == items['Answer']:
        score +=1
        cprint("Correct", "green")
    else:
        cprint(f'Wrong ,The Correct answer is {items["Answer"]}',"red")

print(f'Your Final Score is {score} out of {len(quiz)}')






# second_answer = input ("Which planet is known as the red planet \n A.Earth \n B.Mars \n C.Jupiter \n D.Saturn \n Your answer: ")
# third_answer = input ("What is the largest ocean on the Earth \n A.Atlantic \n B.Indian \n C.Arcitc \n D.Pacific \n Your answer: ")


# go to the next question
# display the correct_answer
# Display the score



# cprint("Hello, World!", "green")
