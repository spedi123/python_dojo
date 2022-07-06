

class Car:
    creator = 'peter'

    def __init__(self, make, model, color='blue'):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False

    def info(self):
        print(f'creator: {self.creator}')
        print(f'make: {self.make}')
        print(f'make: {self.model}')
        print(f'make: {self.color}')
        return self

    def turn_on(self):
        self.is_running = True
        return self

    def drive(self):
        if self.is_running:
            print("driving drinving")
        else:
            print("can't drive")
        return self

    @classmethod
    def change_creator(cls, new_creator):
        cls.creator = new_creator

    @staticmethod
    def is_appropriate_color(color):
        color_list = ['blue', 'white', 'red']
        if color in color_list:
            return True
        else:
            return False


car_a = Car('toyota', 'rav4')
car_b = Car('kia', 'sorento', 'black')
car_c = Car('tesla', 'model3', 'red')

car_a.turn_on()

# print(Car.is_appropriate_color(car_b.color))
# car_a.drive()
# car_b.drive()
# Car.change_creator("esther")

car_a.info()
