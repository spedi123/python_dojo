

class Car:
    def __init__(self, make, model, color='blue'):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False

    def info(self):
        print(f'make: {self.make}')
        print(f'make: {self.model}')
        print(f'make: {self.color}')

    def turn_on(self):
        self.is_running = True

    def drive(self):
        if self.is_running:
            print("driving drinving")
        else:
            print("can't drive")


car_a = Car('toyota', 'rav4')
car_b = Car('kia', 'sorento', 'black')
car_c = Car('tesla', 'model3', 'red')

car_a.turn_on()
car_a.drive()
car_b.drive()

car_a.info()
