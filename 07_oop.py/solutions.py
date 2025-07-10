class Car:
    total_car = 0
    # brand = None     \ not write this
    # model = None
    def __init__(self, brand, model):  # self is same as this # __init__ is like constuctor so its first come
        self.__brand = brand    # if we put __ then it make it private
        self.__model = model     
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " ...!"
    
    # def get_model(self):
    #     return self.__model + " ...!"
    
    def fuel_type(self):  # polymorphism
        return "Petrol or Diesel"
    
    @property   # property decorator make sure that method can not change or override
    def model(self):
        return self.__model
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod  # static methods can access only by class not by objects
    def general_des():
        return "Cars are amazing"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):  # polymorphism
        return "Electic Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")  

print(isinstance(my_tesla,Car))             
print(isinstance(my_tesla,ElectricCar))          
print(my_tesla.brand)   #its now not working because we make it private
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

my_car = Car("Tata", "Safari")
my_car.model = "Honda"
print(my_car.model)

Car("Tata", "Nexon")
# print(safari.fuel_type())
print(Car.total_car)
print(my_car.general_des())
print(Car.general_des())

my_Car = Car("Tata", "Neno") # object
print(my_Car.brand)    
print(my_Car.model)    
print(my_Car.full_name())    


my_new_car = Car("Tata","Safari")
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElecticeCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElecticeCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
# so here multiple Inheritance can possible