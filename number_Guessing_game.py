import random

number = random.randint(1, 200)

guess = None

while(guess != number):
    guess = int(input("Guess a number between 1 - 200: "))
    if(guess > number):
        print("Too high!")
    elif(guess < number):
        print("Too low!")
    
    elif(guess == number):
        print(f"You have guessed the right number! {number}")