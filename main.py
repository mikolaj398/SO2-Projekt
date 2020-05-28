from car import Car
import threading
import curses
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

def main(stdscr):
    stdscr.nodelay(1)
    for i in range(car_count):
        cars.append(Car(str(i), lines, gas_stations, pitstops, tires_change_stations))
    
    stdscr.clear()

    try:
        stdscr.addstr(len(cars)+4, 0, "Nacisnij ESC aby wyjsc.")
        stdscr.addstr(0, 0, "Tablica wynikow:")
        
        for car in cars:
            car.start()
        
        while True:
            sorted_cars = sorted(cars, key= lambda car: car.distance, reverse=True )  
            stdscr.refresh()
            key = stdscr.getch()
            for i in range(len(sorted_cars)):
                stdscr.addstr(i+2, 0, str(sorted_cars[i]))
                stdscr.addstr(i+2, 10, sorted_cars[i].state.ljust(40))
                stdscr.addstr(i+2, 40, sorted_cars[i].get_car_info())
            if key == 27:
                Car.driving = False
                print("Zamykanie wszystkich watkow...")
                break
    except Exception as e:
        print("Informacje o samochodach nie mieszcza sie w konsoli. Powieksz konsole lub zminejsz liczbe samochodow.")
curses.wrapper(main)