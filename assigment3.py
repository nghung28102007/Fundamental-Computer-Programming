#1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1  
#2
try:
    inches = float(input("Enter length in inches: "))
    if inches < 0:
        print("Length cannot be negative.")
    else:
        cm = inches * 2.54
        print(f"{inches} inches is equal to {cm} centimeters.")
except ValueError:
    print("Please enter a valid number.")

#3
import math
try:
    num = input("Enter your list of number: ").split()
    if not num:
        print("The list is empty")
    else:
        print(f"The maximum number is: {max(num)}, and the minimum number is: {min(num)}")
except ValueError:
    print("Please enter valid integers separated by spaces.")
#4
from random import randint
random_number = randint(1, 10)
while True:
    try:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
            break
    except ValueError:
        print("Please enter a valid integer.")
        
#5
correct_username = 'python'
correct_password = 'rules'
def auth(username, password, attempts):
    if username != correct_username:
        print("")

