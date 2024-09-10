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
    










# Create stations (as seperate class in different file) and add the ability to stop at stations.
# They should all be at different distances and reaching them depends on current coal/water/steam levels.
# The distance should be a set number of miles away from the starting station.
# The player should be able to stop at a station and refuel coal and water.
# The player should be able to see the distance to the next station.
# The player should be able to see the total distance traveled.
# The player should be able to see the total distance remaining.
# Stations should have the ability for trains to pick up and drop off passengers.