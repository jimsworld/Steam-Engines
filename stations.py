class Stations:
    def __init__ (self, name, distance, passengers, refuel_coal, refuel_water):
        self.name = name
        self.distance = distance
        self.passengers = passengers
        self.refuel_coal = refuel_coal
        self.refuel_water = refuel_water
    
    def get_distance(self):
        return self.distance
    
    def get_passengers(self):
        return self.passengers
    










# Create stations (as seperate class in different file) and add the ability to stop at stations.
# They should all be at different distances and reaching them depends on current coal/water/steam levels.
# Stations should have a name.
# The distance should be a set number of miles away from the starting point.
# The player should be able to stop at a station and refuel coal and water.
# The player should be able to see the distance to the next station.
# The player should be able to see the total distance traveled.
# The player should be able to see the total distance remaining.
# Stations should have the ability for trains to pick up and drop off passengers.