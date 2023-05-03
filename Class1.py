class SedanCar:
    def __init__(self, hp, color, fuel, gearbox):
        self.horsepower = hp
        self.gearbox = gearbox
        self.color = color
        self.fuel = fuel
        self.rpm = 0

    def car_horn(self):
        print("Boooooogh!!!")

    def car_break(self):
        print("Break!!!")

    def car_accelerate(self, value):
        for i in range(value):
            self.rpm += 1000
        print("Current round per minute :", self.rpm)


samand = SedanCar(113, "black", 60, "Manual")  # Create an instance of class SedanCar
dena = SedanCar(113, "white", 55, "Auto")
# samand.car_accelerate()  # Calling a method of object samand
# print(dena.gearbox)
# print(samand.horsepower)
dena.car_accelerate(5)  # Calling a method of object dena with 5 as argument
