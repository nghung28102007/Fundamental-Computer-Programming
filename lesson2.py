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
try:
    work_hours = float1(input("Enter hours worked: "))
    hourly_rate = float1(input("Enter hourly rate: "))
    
    if work_hours > 40:
        total_pay = (40 * hourly_rate) +((work_houurs - 40) * hourly_rate * 1.5)
    else:
        total_pay = work_hours * hourly_rate
    print("Total pay: " + str(total_pay))
except:
    print("Error, please enter numeric input")


