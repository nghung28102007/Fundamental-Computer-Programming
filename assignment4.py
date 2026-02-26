#1
numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Top 5 greatest numbers:")
for num in numbers[:5]:
    print(num)
#2
num = int(input("Enter an integer: "))

if num < 2:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

#3
cities = []

for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

print("\nCities you entered:")
for city in cities:
    print(city)

#4
def sum_list(numbers):
    return sum(numbers)
my_list = [3, 5, 7, 2, 8]
result = sum_list(my_list)
print("Sum of the list:", result)

#5
def remove_odd(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

original_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_odd(original_list)

print("Original list:", original_list)
print("Even numbers only:", new_list)