#1
import re
def code_check(course_code):
    search = r'^[A-Z]{2,3}\d{3}$'
    if re.fullmatch(search, course_code):
        return True
    else:
        return False
print(code_check("TEC001")) # test

#2
import re 
def color_check(color_code):
    search1 = r'^#[A-F0-9]{6}$'
    if re.fullmatch(search1, color_code):
        return True
    else:
        return False
    
print(color_check("#CG84387238")) # test

#3
def paragraph_sum(paragraph):
    search2 = r'\d+'
    number_str = re.findall(search2, paragraph)
    tong = 0
    for i in number_str:
        tong += int(i)
    return tong
paragraph = input("Enter your string:")
print(paragraph_sum(paragraph))

#4
def hide_number(inp):
    search3 = r'\+84|\d{10}'
    substitute = re.sub(search3, '*', inp)
    print(substitute)

hide_number("+84 bla bla 0846281007") #test

#5
from random import uniform
def cal_pi():
    N = int(input("How many points:"))
    n = 0
    for i in range(N):
        x = uniform(-1, 1)
        y = uniform(-1, 1)

        if x**2 + y**2 < 1:
            n += 1
    pi = 4 * n / N
    print(pi)
cal_pi()

    










    


    
    


