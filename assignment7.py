#1, 2 ,3
class Car:
    def __init__(self, regis_num, max_speed):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dis = 2000

    def test(self):
        print(f"The registration number of car is : {self.regis_num}, current speed is :{self.current_speed}, max speed is: {self.max_speed}, the amount of travelled distance is: {self.travelled_dis}")
    
    def accelerate(self, change):
        self.current_speed += change
        
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"Current speed after accelerating is: {self.current_speed}")

    def drive(self, time):
        travelled = self.current_speed * time
        self.travelled_dis += travelled
        print(f"Current travelled distance is: {self.travelled_dis}")





car1=  Car("ABC-123", 142)     
car1.test()
car1.accelerate(60)
# car1.accelerate(70)
# car1.accelerate(50)
# car1.accelerate(-200)
car1.drive(1.5)


#4
from random import randint
class RaceCar:
    def __init__(self,registration_number, max_speed2):
        self.registration_number = registration_number
        self.travelled_distance = 0
        self.current_speed = 0
        self.max_speed2 = max_speed2
    def accel(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.max_speed2:
            self.current_speed = self.max_speed2
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance
car_list = []
for i in range(11):
    plate = f'ABC-{i}'
    random_max_speed = randint(150, 200)
    new_car = RaceCar(plate, random_max_speed)
    car_list.append(new_car)
    print(f'Car regis number is: {new_car.registration_number}, max speed of this car is: {new_car.max_speed2} km') 
    

while max(car.travelled_distance for car in car_list) < 10000:
    for car in car_list:
        speed_change = randint(-10, 15)
        car.accel(speed_change)
        car.drive(1)
print(f"{'Regis num': <15} | {'Max speed' :<10} | {'Distance travelled': <12}")
print("-" * 50)
for x in car_list:
    print(f"{x.registration_number:<15} | {x.max_speed2:<10} | {x.travelled_distance:<12}")

