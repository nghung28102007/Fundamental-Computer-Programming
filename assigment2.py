#1
least_size = 42
size = float(input("Enter the size: "))
def check_size(size):
    if size < least_size:
        print("release the fish back into the lake" ,  f"and {least_size - size:.2f}cm more is required")
    else:
        print("keep the fish")
check_size(size)

#2
cabin_class = input("Enter cabin class (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Error: Invalid cabin class.")
#3
biological_sex =  input("Enter biological sex (Males/Females): ").upper()
hemoglobin_level = float(input("Enter hemoglobin level (g/dL): "))
def check_hemoglobin(biological_sex, hemoglobin_level):
    if biological_sex == "MALES":
        if hemoglobin_level < 117:
            print("The hemoglobin level is low. ")
        elif 117 <= hemoglobin_level <= 155:
            print("The hemoglobin level is normal. ")
        else:
            print("The hemoglobin level is high. ")
    elif biological_sex == "FEMALES":
        if hemoglobin_level < 134:
            print("The hemoglobin level is low. ")
        elif 134 <= hemoglobin_level <= 167:
            print("The hemoglobin level is normal. ")
        else:
            print("The hemoglobin level is high. ")

check_hemoglobin(biological_sex, hemoglobin_level)
#4
year = int(input("Enter a year: ")) 
def check_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
check_year(year)
#5
from math import pi
def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = pi * (radius ** 2) / 10000
    unit_price = price / area
    return unit_price

diameter1 = float(input("Enter diameter of pizza 1 (in cm): "))
price1 = float(input("Enter price of pizza 1: "))
diameter2 = float(input("Enter diameter of pizza 2 (in cm): "))
price2 = float(input("Enter price of pizza 2: "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("Pizza 1 offers a better value.")
elif unit_price2 < unit_price1:
    print("Pizza 2 offers a better value.")
else:
    print("Both pizzas offer the same value.")
