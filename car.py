import threading
import time
import random

class Car(threading.Thread):
    driving = True

    def __init__(self, number ,avaiable_lines, gas_stations, pitstops, tires_change_stations):
        threading.Thread.__init__(self)
        self.number = number
        self.lane = -1
        self.state = ''

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
                self.state = f"Jedzie na torze: {line}"
                self.drive()
                self.avaiable_lines[line].release()
                continue
            gas_station, aviable = self.check_avaiable_gas_stations()
            if aviable and self.fuel<=0:
                self.gas_stations[gas_station].acquire()
                self.state = f"Tankuje na stacji numer: {gas_station}"
                self.fill_tank()
                self.gas_stations[gas_station].release()
                continue
            pitstop, aviable = self.check_avaiable_pitstops()
            if aviable and self.car_durability<=30:
                self.pitstops[pitstop].acquire()
                self.state = f"Jest w pitstopie numer: {pitstop}"
                self.use_pitstop()
                self.pitstops[pitstop].release()
                continue
            tires_change_station, aviable = self.check_avaiable_tiers_change_stations()
            if aviable and self.tires_durability<=30:
                self.tires_change_stations[tires_change_station].acquire()
                self.state = f"Zmienia opony przy stacji: {tires_change_station}"
                self.change_tires()
                self.tires_change_stations[tires_change_station].release()
                continue
            self.state = "Czeka"
            time.sleep(random.uniform(1, 5))
                
    def drive(self):
        self.distance += random.randint(1,3)
        self.fuel -= random.randint(10,40)
        if self.fuel < 0: self.fuel=0 
        self.car_durability -= random.randint(10,60)
        if self.car_durability < 0: self.car_durability=0 
        self.tires_durability -= random.randint(5,20)
        if self.tires_durability < 0: self.tires_durability=0 
        time.sleep(random.uniform(1, 5))

    def fill_tank(self):
        self.fuel = 100
        time.sleep(random.uniform(1, 5))

    def use_pitstop(self):
        self.car_durability = 100
        time.sleep(random.uniform(1, 5))

    def change_tires(self):
        self.tires_durability = 100
        time.sleep(random.uniform(1, 5))

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
    
    def __str__(self):
        return f"Bolid {self.number}"

    def get_car_info(self):
        distance = f"Pokonany dystans: {self.distance}".ljust(21)
        fuel = f"Stan paliwa: {self.fuel}".ljust(17)
        car_durability = f"Stan samochodu: {self.car_durability}".ljust(20)
        tires_durablity = f"Stan opon: {self.tires_durability}".ljust(20)

        return f"{distance} {fuel} {car_durability} {tires_durablity}"
