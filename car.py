import threading
import time
import random

class Car(threading.Thread):
    driving = True

    def __init__(self, number ,avaiable_lines, gas_stations, pitstops, tires_change_stations):
        threading.Thread.__init__(self)
        self.number = number
        self.lane = -1

        self.avaiable_lines = avaiable_lines
        self.gas_stations = gas_stations
        self.pitstops = pitstops
        self.tires_change_stations = tires_change_stations

        self.distance = 0
        self.fuel = 100
        self.car_durability = 100
        self.tires_durability = 100

    def run(self):
        while self.driving:
            line, aviable = self.check_avaiable_lanes()
            if aviable and self.fuel>0 and self.car_durability>0 and self.tires_durability>0:
                self.avaiable_lines[line].acquire()
                self.line = line
                self.drive()
                self.avaiable_lines[line].release()
                continue
            gas_station, aviable = self.check_avaiable_gas_stations()
            if aviable and self.fuel<=0:
                self.gas_stations[gas_station].acquire()
                self.fill_tank()
                self.gas_stations[gas_station].release()
                continue
            pitstop, aviable = self.check_avaiable_pitstops()
            if aviable and self.car_durability<=30:
                self.pitstops[pitstop].acquire()
                self.use_pitstop()
                self.pitstops[pitstop].release()
                continue
            tires_change_station, aviable = self.check_avaiable_tiers_change_stations()
            if aviable and self.tires_durability<=30:
                self.tires_change_stations[tires_change_station].acquire()
                self.change_tires()
                self.tires_change_stations[tires_change_station].release()
                continue
            print(f"car {self.number} is no able to drive. Distance {self.distance}. Fuel: {self.fuel}. Car durability {self.car_durability}. Tires durability: {self.tires_durability}.")
            time.sleep(random.uniform(1, 5))
                
    def drive(self):
        self.distance += 1
        self.fuel -= 50
        self.car_durability -= 60
        self.tires_durability -= 25
        print(f"car {self.number} is driving on line {self.line}. Distance {self.distance}. Fuel: {self.fuel}. Car durability {self.car_durability}. Tires durability: {self.tires_durability}.")
        time.sleep(random.uniform(1, 2))

    def fill_tank(self):
        self.fuel = 100
        print(f"car {self.number} is getting gas. Distance {self.distance}. Fuel: {self.fuel}. Car durability {self.car_durability}. Tires durability: {self.tires_durability}.")
        time.sleep(random.uniform(1, 2))

    def use_pitstop(self):
        self.car_durability = 100
        print(f"car {self.number} is using pitstop. Distance {self.distance}. Fuel: {self.fuel}. Car durability {self.car_durability}. Tires durability: {self.tires_durability}.")
        time.sleep(random.uniform(1, 2))

    def change_tires(self):
        self.tires_durability = 100
        print(f"car {self.number} is changed tires. Distance {self.distance}. Fuel: {self.fuel}. Car durability {self.car_durability}. Tires durability: {self.tires_durability}.")
        time.sleep(random.uniform(1, 2))

    def check_avaiable_lanes(self):
        for i in range(len(self.avaiable_lines)):
            if not self.avaiable_lines[i].locked():
                return i, True
        return -1, False

    def check_avaiable_gas_stations(self):
        for i in range(len(self.gas_stations)):
            if not self.gas_stations[i].locked():
                return i, True
        return -1, False

    def check_avaiable_pitstops(self):
        for i in range(len(self.pitstops)):
            if not self.pitstops[i].locked():
                return i, True
        return -1, False

    def check_avaiable_tiers_change_stations(self):
        for i in range(len(self.tires_change_stations)):
            if not self.tires_change_stations[i].locked():
                return i, True
        return -1, False
