class Car :
    total_car = 0 
    def __init__(self , brand , model):
        self.__brand = brand 
        self.model = model 
        Car.total_car +=1
    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self) :
        return "petrol or diesel"
    

    @staticmethod
    def general_description():
        return "cars are a means of transport"
        

class ElectricCar(Car): 
    def __init__(self , brand, model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size 
    
    def fuel_type(self) :
        return "Electric Charge"

my_Tesla = ElectricCar("Tesla" , "Model X" , "85kWh")
# print(my_Tesla.__brand)
# print(my_Tesla.fuel_type())
# my_car = Car("Toyota" , "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# another_car = Car("Honda" , "Civic")
# print(another_car.brand)
# print(another_car.model)
safari = Car("Tata" , "Safari")
safariThree = Car("Tata" , "Nexon")
# print(safari.fuel_type())
print(Car.total_car)
print(safari.general_description())
print(Car.general_description())