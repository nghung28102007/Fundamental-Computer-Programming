class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bot = bottom_floor
        self.top = top_floor
        self.current = bottom_floor
    def go_to_floor(self, target_floor):
        self.target = target_floor
        while self.current < self.target:
            self.floor_up()
        while self.current > self.target:
            self.floor_down()

    def floor_up(self):
        self.current = self.current + 1
        print(f"Current floor is {self.current}")
    def floor_down(self):
        self.current = self.current - 1
        print(f"Current floor is {self.current}")

h = Elevator(0, 10) 
h.go_to_floor(5)