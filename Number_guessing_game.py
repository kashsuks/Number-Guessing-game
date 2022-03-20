import math
import random


number_to_guess = random.randrange(1, 11)
Total_Chances = int(input("How many chances do you want?: "))
Wrong_answers = 0
random_list = range(1, Total_Chances + 1)
Tries_left = Total_Chances - 1
print("Your guess needs to be between 1 and 10")

for number in random_list:
    guess = int(input("Enter your guess here: "))
    if guess == number_to_guess:
        print("Congratulations!! Your guess was correct!")
        exit()
    else:
        print("Your guess was wrong!")
        print(f"You have {Tries_left} tries left")
        Total_chances = Total_Chances - 1
        Tries_left = Tries_left - 1
        if guess > number_to_guess:
            print("Your guess was higher than the number to guess")
        else:
            print("Your guess was lower than the number to guess")
        

if Tries_left == - 1:
    print("Game over, You have 0 tries left")
    print(f"The correct answer was {number_to_guess}!")

