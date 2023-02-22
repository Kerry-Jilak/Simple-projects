#this game is rock paper scissors
import random

user_score=0
computer_score=0
options=['rock','paper','scissors']
while True:
     user_guess=input('Pick Rock/Paper/Scissors or q to end ').lower()
     if user_guess=='q':
        break
     if user_guess not in options:
        continue
    #continue will send us back to the input place
    #we use while so that if the condition is still true,we iterate the code
     r=random.randint(0,2)
     computer_guess=options[r]
     print('The computer chose',computer_guess+'.')
     if user_guess=='scissors' and computer_guess=='rock':
        print('You won!')
        user_score+=1
     elif user_guess=='paper' and computer_guess=='rock':
        print('You won!')
        user_score+=1
     elif user_guess=='scissors' and computer_guess=='paper':
        print('You won!')
        user_score+=1
     else:
        print('The Computer won!')
        computer_score+=1
print('You won with',user_score,'points')
print('The computer won',computer_score,'points')



    



