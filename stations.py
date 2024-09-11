import random

class Stations:
    def __init__ (self, name, distance):
        self.name = name
        self.distance = distance
        self.passengers = random.randint(0, 30)
        self.refuel_coal = random.randint(0, 10)
        self.refuel_water = random.randint(0, 10)
    
    def get_distance(self):
        return self.distance
    
    def get_passengers(self):
        return self.passengers
    
    def get_current_station(self):
        return self.name
    
    def distance_to_next_station(self, next_station):
        return abs(self.distance - next_station.get_distance())


# Station list
station_01 = Stations("Tywyn Wharf", 0)
station_02 = Stations("Pendre", 0.42)
station_03 = Stations("Rhydyronen", 2.15)
station_04 = Stations("Brynglas", 3.18)
station_05 = Stations("Dolgoch", 4.90)
station_06 = Stations("Abergynolwyn", 6.57)
station_07 = Stations("Nant Gwernol", 7.25)
station_list = [station_01, station_02, station_03, station_04, station_05, station_06, station_07]



# add in the method from current_station to next_station

# Create the ability to stop at stations.
# Reaching them depends on current coal/water/steam levels and the distance to the next station.
# The player should be able to stop at a station and refuel coal and water.
# The player should be able to see the distance to the next station.
# The player should be able to see the total distance traveled.
# The player should be able to see the total distance remaining.
# Stations should have the ability for trains to pick up and drop off passengers.