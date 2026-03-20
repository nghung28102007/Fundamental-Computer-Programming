#1
number = []
while True:
    user_input = input("Enter your list of number(press Enter to exit):")
    if user_input == "":
        break
    try:
        num = float(user_input)
        number.append(num)
    except ValueError:
        print("You need to enter a number:")

number.sort(reverse=True)
print("Top 5 greatest number:")
for i in number[:5]:
    print(number)

#2
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month (1-12): "))

if month == 12 or month == 1 or month == 2:
    print(seasons[0])
elif 3 <= month <= 5:
    print(seasons[1])
elif 6 <= month <= 8:
    print(seasons[2])
elif 9 <= month <= 11:
    print(seasons[3])
else:
    print("Invalid month number.")
#3
names = set()

while True:
    name = input("Enter a name: ")
    if name == "":
        break
    
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nList of names:")
for n in names:
    print(n)
#4
def word_frequency(text):
    words = text.lower().split()
    total_words = len(words)
    counts = {}

    for w in words:
        counts[w] = counts.get(w, 0) + 1

    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
    top_5 = dict(sorted_words)
    
    sum_top_5 = sum(top_5.values())
    proportion = (sum_top_5 / total_words) * 100

    print(f"Top 5: {top_5}")
    print(f"Total number of words: {total_words}")
    print(f"Proportion: {sum_top_5} / {total_words} = {proportion:.2f}%")


text_input = "apple banana apple orange apple banana grape apple pineapple orange"
word_frequency(text_input)
#test

#5
def remove_odd_numbers(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_odd_numbers(original_list)

print(f"Original list: {original_list}")
print(f"Cut-down list: {cut_down_list}")



