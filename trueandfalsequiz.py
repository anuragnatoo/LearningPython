import time
print("Hello! Welcome to the True and False Quiz!")
time.sleep(2)
name = input("What's your name? : ")
# time.sleep(2)
print("Hey! "+name+"\nDo you want to know how to play or Get started\nType Y for Rules and N to start playing!")
time.sleep(3)
answer = input()
if answer.lower()=="Y".lower():
    print("Okay!\n You will be asked a few questions you need to answer True or False!\n")
    time.sleep(1)
else:
    print("Cool! Let's get started\n")
    time.sleep(1)
score = 0
time.sleep(2)
print("Manmohan Singh is the current Prime Minister of India")
answer1 = input("Enter T or F : ")
if answer1.lower() == "T".lower():
    print("You are incorrect\nBetter luck for the next Question "+name+" Your score is ", score)
elif answer1.lower() == "F".lower():
    score = score+1
    print("Good! You scored a point!\nAnd your score is", score)
time.sleep(2)
print("Donald Trump is the current President of the U.S.A")
answer1 = input("Enter T or F : ")
if answer1.lower() == "F".lower():
    print("You are incorrect\nBetter luck for the next Question "+name+" Your score is ", score)
elif answer1.lower() == "T".lower():
    score = score+1
    print("Good! You scored a point!\nAnd your score is", score)
time.sleep(2)
print("New Delhi is the capital of India")
answer1 = input("Enter T or F : ")
if answer1.lower() == "F".lower():
    print("You are incorrect\nBetter luck for the next Question "+name+" Your score is ", score)
elif answer1.lower() == "T".lower():
    score = score+1
    print("Good! You scored a point!\nAnd your score is", score)