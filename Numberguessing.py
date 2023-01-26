import random
from module_for_7 import day12
print(day12)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

n = random.randint(1,100)
print(n)
d = input("Choose a difficulty. Type 'easy' or 'hard':")
if d == 'easy':
    print("You have 10 attempts")
    no_of_attempts = 10
    while no_of_attempts :
     guess = int(input("Make a guess: "))

     if guess < n and no_of_attempts != 1:
        print("Too low")
        no_of_attempts -= 1
        print(f"You have {no_of_attempts} attempts left to guess the number.\n")

     elif guess > n and no_of_attempts != 1:
        print("Too high")
        no_of_attempts -= 1
        print(f"You have {no_of_attempts} attempts left to guess the number.\n")

     elif guess == n:
        print("Bulls eye. You win")
        right = (10 - no_of_attempts) + 1
        print(f"You guessed this in {right} attempt\n")
        exit()

     if no_of_attempts == 0:
            print("You have runned out of guesses. You loose")

elif d == 'hard':
    print("You have 5 attempts")
    no_of_attempts2 = 5
    while no_of_attempts2 :
     guess = int(input("Make a guess: "))

     if guess < n:
        print("Too low")
        no_of_attempts2 -= 1
        print(f"You have {no_of_attempts2} attempts left to guess the number.\n")
     elif guess > n:
        print("Too high")
        no_of_attempts2 -= 1
        print(f"You have {no_of_attempts2} attempts left to guess the number.\n")

     elif guess == n:
        print("Bulls eye. You win")
        right = (5 - no_of_attempts2) + 1
        print(f"You guessed this in {right} attempt\n")
        exit()
     if no_of_attempts2 == 0:
         print("You have runned out of guesses. You loose")

else:
    print("Invalid input")
    exit()
