from turtle import Turtle
import random

CAR_COLORS = ["grey","red","blue","green","purple","orange","pink","violet","brown","yellow"]

class Vehicle:
    def __init__(self):
        super().__init__()
        self.all_vehicles = []
        self.increase_speed = 1
        self.vehicle_speed = 20
    def create_vehicles(self):
        rand_num = random.randint(1,4)   #remember when writing randint(should be negative or smaller, should be positve or greater)
        if rand_num == 1:
            new_vehicle = Turtle("square")
            new_vehicle.shapesize(stretch_len= 2,stretch_wid= 1)
            new_vehicle.penup()
            new_vehicle.color(random.choice(CAR_COLORS))
            random_y = random.randint(-180,200)
            new_vehicle.goto(300,random_y)
            self.all_vehicles.append(new_vehicle)
    def car_forward(self):
        new_speed = self.vehicle_speed + self.increase_speed
        for car in self.all_vehicles:
            car.backward(new_speed)
    def increase_vehicle_speed(self):
        self.increase_speed += 1