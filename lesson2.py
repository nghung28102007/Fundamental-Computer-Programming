#1
user_hours = int(input("Enter hours: "))
user_rate = float(input("Enter rate: "))
gross_pay = user_hours * user_rate
print("Gross pay: " + str(gross_pay))
#2
story_name = input("Enter your name: ")
story_year = int(input("Enter your birth year: "))
print(f"{story_name} is a vliant knight, borin in the year {story_year}. One morning, {story_name} woke up to an awful racket: a dragon was approaching the village. Only {story_name} could save the village's residents.")

#3
work_hour = int(input("Enter the number of hours worked in a week: "))
hourly_rate = float(input("Enter the hourly pay rate: "))
if work_hour > 40:
    pay = work_hour * hourly_rate + (work_hour - 40) * (hourly_rate * 0.5)
else:
    pay = work_hour * hourly_rate
print("Total weekly pay: " + str(pay))

try:
    if work_hour < 0 or hourly_rate < 0:
        raise ValueError("Negative values are not allowed.")
except ValueError as e:
    print(e)

try:
    if 
