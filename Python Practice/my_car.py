from car import Car
from electric_car import Electric_car as EC

my_new_car = Car("Hyundai", "Santa Fe", "2020")
print(my_new_car.get_description_name())
my_new_car.update_mileage(23)
my_new_car.increment_miles(1000)
my_new_car.increment_miles(1000)
my_new_car.read_odometer()
my_new_ecar = EC("Hyundai", "Sante Fe", "2026")
print(my_new_ecar.get_description_name())
car_battery = my_new_ecar.battery = 65
print(car_battery)



