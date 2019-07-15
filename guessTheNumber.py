import random
import time
guesscount=0
print("Hey! Welcome to the Game Guess the Number!\n What's your Name?")
time.sleep(1)
name=input()
print("Hey",name.title(),"Do you want to know the rules? Or Get Started?\n Press Y for Rules and N for getting started!")
choice = input()
if choice.lower() == 'y':
    print("Okay! I'll think of a number and you have to guess in a fixed number of tries")
    print("You can decide the range")
print("Please enter the range you want to choose!")
print("The choices are\n1)1 to 30---and you get 4 tries for guessing the number")
print("2)1 to 100----and you get 8 tries for guessing the number")
print("3)1 to 500----and you get 15 tries for guessing the number")
print('Please enter the range you want!')
range1 = int(input())
if range1 == 1:
    tries = 4
    number = random.randint(1,30)
elif range1 == 2:
    tries = 8
    number = random.randint(1,100)
elif range1 == 3:
    tries =15
    number = random.randint(1,500)
#print(number)
count = 0
for count in range(tries):
    print('Take a guess')
    guess = int(input())
    if guess < number :
        print("Your guess is too low!")
    if guess > number :
        print('Your guess is too high!')
    if guess == number:
        break
if guess == number:
    count = count+1
    print("Great!",name.title(),"You guessed my number in",count,"tries!")
if guess !=number:
    print("Nope! I was thinking of",number)
    print("Better luck next time!")
