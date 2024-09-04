from global_time import GlobalTime

# Initialize global time
global_time = GlobalTime()

class Loco_Steam:
    def __init__(self, name, current_speed, max_speed, current_coal, current_water, current_steam, max_coal, max_water, max_steam):
        self.on = False
        self.name = name
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.current_coal = current_coal
        self.current_water = current_water
        self.current_steam = current_steam
        self.max_coal = max_coal
        self.max_water = max_water
        self.max_steam = max_steam

    def start_engine(self):
        self.on = True

    def stop_engine(self):
        self.on = False

    def enforce_non_negative(self):
        self.current_speed = max(0, self.current_speed)
        self.current_coal = max(0, self.current_coal)
        self.current_water = max(0, self.current_water)
        self.current_steam = max(0, self.current_steam)

    def add_water(self, amount):
        self.current_water += amount
        if self.current_water > self.max_water:
            self.current_water = self.max_water
    
    def add_coal(self, amount):
        self.current_coal += amount
        if self.current_coal > self.max_coal:
            self.current_coal = self.max_coal
    
    def make_steam(self):
        if self.on and self.current_coal > 0 and self.current_water > 0:
            self.current_coal -= 1
            self.current_water -= 1
            self.current_steam += 1
            self.enforce_non_negative()
            if self.current_steam > self.max_steam:
                self.current_steam = self.max_steam
    
    def accelerate(self):
        if self.on and self.current_steam > 0:
            self.current_speed += 1
            self.current_steam -= 1
            self.enforce_non_negative()
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
    
    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 1
            self.enforce_non_negative()
    
    def get_speed(self):
        return self.current_speed
    
    def get_resources(self):
        return self.current_coal, self.current_water, self.current_steam