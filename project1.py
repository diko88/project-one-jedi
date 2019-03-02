# Project #1 - Jedi
# - Create a Python project that will immitate a Jedi seeking advice from master Yoda.
# 	- Allow the Jedi user to input their question
# 	- Show an in progress message
# 	- Create 10 responses from master Yoda, and show a random response
# 	- Allow the Jedi user to ask another question/advice or quit the game

import random
question = input("What is your question? ")
print("Yoda is thinking about it...")

responses = ['yes it is', 'No', 'Who knows', 'The time is now',
             'I do not know', 'All you need is love', 'you are a noob', 'Maybe', 'Today']

response = random.choice(responses)
print("Yoda's answer is : ", response)

while True:
    answer = input('Do you have another question or need another advice? ')
    if answer == 'yes':
        another_q = input("Ask another question ")
        new_response = random.choice(responses)
        print("Yoda's answer is : ", new_response)

    else:
        print('Goodbye')
        break
