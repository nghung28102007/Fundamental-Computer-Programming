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
max_attempts = 5
def auth(attempts):
    if attempts > max_attempts:
        print("Access denied.")
        return
    
    username = input("Enter your username:")
    password = input("Enter your password:")
    
    if username == correct_username and password == correct_password:
        print("Welcome")
    else:
        print(f"You have {max_attempts - attempts - 1 } tries left")
        auth(attempts + 1) 
auth(1) #enter the number of attempt 0-5

#6
inp_str = input("Enter your string:")
if len(inp_str) % 2 == 0:
    print(inp_str[len(inp_str) // 2  : len(inp_str) // 2 + 2])
else:
    print(inp_str[len(inp_str) // 2])

#7
def acronym(str):
    words = str.split()
    acronym = ""

    for i in words:
        letter = i[0].upper()
        acronym += letter
    print(acronym)


acronym("viet nam")
    




        

