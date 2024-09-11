from global_time import GlobalTime

# Initialize global time
global_time = GlobalTime()

class Loco_Steam:
    def __init__(self, name, current_coal, current_water, current_steam, current_speed, max_coal, max_water, max_steam, max_speed):
        self.on = False
        self.name = name      
        self._current_coal = current_coal
        self._current_water = current_water
        self._current_steam = current_steam
        self._current_speed = current_speed
        self.max_coal = max_coal
        self.max_water = max_water
        self.max_steam = max_steam
        self.max_speed = max_speed

    @property
    def current_coal(self):
        return self._current_coal
    
    @current_coal.setter
    def current_coal(self, value):
        self._current_coal = max(0, value)

    @property
    def current_water(self):
        return self._current_water
    
    @current_water.setter
    def current_water(self, value):
        self._current_water = max(0, value)
    
    @property
    def current_steam(self):
        return self._current_steam
    
    @current_steam.setter
    def current_steam(self, value):
        self._current_steam = max(0, value)
    
    @property
    def current_speed(self):
        return self._current_speed
    
    @current_speed.setter
    def current_speed(self, value):
        self._current_speed = max(0, value)

    def start_engine(self):
        self.on = True

    def stop_engine(self):
        self.on = False

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
            if self.current_steam > self.max_steam:
                self.current_steam = self.max_steam
    
    def accelerate(self):
        if self.on and self.current_steam > 0:
            self.current_steam -= 1
            self.current_speed += 1
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
        else:
            self.current_speed -= 1
    
    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 1
    
    def get_speed(self):
        return self.current_speed
    
    def get_resources(self):
        return self.current_coal, self.current_water, self.current_steam


# Locomotive list
loco_01 = Loco_Steam("Talyllyn", 0, 0, 0, 0, 10, 10, 10, 10)
loco_02 = Loco_Steam("Dolgoch", 0, 0, 0, 0, 8, 10, 10, 12)
loco_list = [loco_01, loco_02]