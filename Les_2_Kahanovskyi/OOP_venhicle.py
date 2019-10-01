class Vehicle:

    NUM_OF_DOORS = 4
    FUEL_TYPE = 'Gas'


    def move(self):

        print(' Car drives ')


    def set_fuel(self, value):

        self._fuel += value


    def get_fuel(self):

        return self._fuel


    def get_brand(self):
        return self._brand


    def set_brand(self, value):
        self._brand = value


    def get_engine(self):
        return self._engine


    def set_engine(self, value):
        self._engine = value


    def get_num_of_wheels(self):

        return self._wheels


    def get_num_of_passengers(self):

        return self._passengers

    def set_num_of_passengers(self, value):

        self._passengers = value


    def __str__(self): # описание объекта

        return f' Brand is {self._brand}, engine is {self._engine} and in this car {self._passengers} passengers '


class Car(Vehicle):

    def __init__(self, brand, engine, wheels, passengers):

        self._brand = brand
        self._engine = engine
        self._fuel = 0
        self._wheels = 4
        self._passengers = passengers


    def move(self):

        print(' Move about 100 km per hour')


    def set_num_of_passengers(self, value):

        if value < 1 or value > 4:

            raise Exception(' count_of_pas_exception ')

        else:

            self._passengers = value


class Truck(Vehicle):

    def __init__(self, brand, engine, wheels, passengers):

        self._brand = brand
        self._engine = engine
        self._fuel = 0
        self._wheels = 8
        self._passengers = passengers

    def move(self):

        print(' Move about 100 km per hour')

    def set_num_of_passengers(self, value):

        if value < 1 or value > 8:

            raise Exception(' count_of_pas_exception ')

        else:

            self._passengers = value


car = Car(' BMW ', ' v8 ', 4, 3)
truck = Truck( 'VAZ ', 'v6', 8, 5)

print(car.get_brand())
car.move()
car.set_num_of_passengers(3)

truck.set_num_of_passengers(6)

print(car)
print(truck)
