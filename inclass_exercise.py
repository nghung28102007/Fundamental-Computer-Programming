import random
random_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
print("Welcome to the Number Guessing Game!")
while attempts < max_attempts:
    try:
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        if user_guess < 1 or user_guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        attempts += 1
        if user_guess < random_number:
            print("Too low!")
        elif user_guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")