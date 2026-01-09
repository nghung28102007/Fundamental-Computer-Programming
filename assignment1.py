#2 
name = input("Enter your name: ")
print(f"Hello, {name}")
#3
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("The circumference of the circle is: " + str(circumference))
#4
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("The perimeter of the rectangle is: " + str(perimeter))
print("The area of the rectangle is: " + str(area))
#5
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_numbers = num1 + num2 + num3
product = num1 * num2 * num3
average = sum_numbers / 3
print("The sum of the numbers is: " + str(sum_numbers))
print("The product of the numbers is: " + str(product))
print("The average of the numbers is: " + str(average))
#6
talents = int(input("Enter the mass in talents: "))
pounds = int(input("Enter the mass in pounds: "))
lots = int(input("Enter the mass in lots: "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"The mass is {kilograms} kilograms and {grams:.2f} grams.")

#7
import random
code3number = ""
for i in range (3):
    code3number += str(random.randint(0,9))
print("Your 3-digit code is: " + code3number)
code4number = ""
for i in range (4):
    code4number += str(random.randint(1,6))
print("Your 4-digit code is: " + code4number)
in


