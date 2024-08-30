from global_time import GlobalTime

# Initialize global time
global_time = GlobalTime()

class Loco_Steam:
    def __init__(self, name, current_speed, top_speed, coal, water, steam, max_coal, max_water, max_steam):
        self.on = False
        self.name = name
        self.current_speed = current_speed
        self.top_speed = top_speed
        self.coal = coal
        self.water = water
        self.steam = steam
        self.max_coal = max_coal
        self.max_water = max_water
        self.max_steam = max_steam

    def start_engine(self):
        self.on = True

    def stop_engine(self):
        self.on = False

    def enforce_non_negative(self):
        self.current_speed = max(0, self.current_speed)
        self.coal = max(0, self.coal)
        self.water = max(0, self.water)
        self.steam = max(0, self.steam)

    def add_water(self, amount):
        self.water += amount
        if self.water > self.max_water:
            self.water = self.max_water
    
    def add_coal(self, amount):
        self.coal += amount
        if self.coal > self.max_coal:
            self.coal = self.max_coal
    
    def make_steam(self):
        if self.on and self.coal > 0 and self.water > 0:
            self.coal -= 1
            self.water -= 1
            self.steam += 1
            self.enforce_non_negative()
            if self.steam > self.max_steam:
                self.steam = self.max_steam
    
    def accelerate(self):
        if self.on and self.steam > 0:
            self.current_speed += 1
            self.steam -= 1
            self.enforce_non_negative()
            if self.current_speed > self.top_speed:
                self.current_speed = self.top_speed
    
    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 1
            self.enforce_non_negative()
    
    def get_speed(self):
        return self.current_speed
    
    def get_resources(self):
        return self.coal, self.water, self.steam