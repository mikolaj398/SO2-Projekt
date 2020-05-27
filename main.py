from car import Car
import threading

def fill_locks_array(array, count):
    for i in range(count):
        array.append(threading.Lock())

car_count = int(input("Podaj liczbe samochodow:"))
lines_count = int(input("Podaj liczbe torow:"))
pitstops_count = int(input("Podaj liczbe dostepnych pit-stopow:"))
tires_change_stations_count = int(input("Podaj liczbe dostepnnych stacji zmiany opon:"))
gas_stations_count = int(input("Podaj liczbe dostepnych stacji do tankowania:"))

cars = []
lines = []
pitstops = []
tires_change_stations = []
gas_stations = []

fill_locks_array(lines, lines_count)
fill_locks_array(pitstops, pitstops_count)
fill_locks_array(tires_change_stations, tires_change_stations_count)
fill_locks_array(gas_stations, gas_stations_count)

for i in range(car_count):
    cars.append(Car(str(i), lines, gas_stations, pitstops, tires_change_stations))

for car in cars:
        car.start()
