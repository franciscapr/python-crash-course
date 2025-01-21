from car import Car
from electric_car2 import ElectricCar

my_mustang = Car('for', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# --- Otra manera de importaciòn ---

#import car

#my_mustang = car.Car('ford', 'mustang', 2024)
#print(my_mustang.get_descriptive_name())

#my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())

