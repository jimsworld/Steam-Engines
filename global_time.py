from datetime import datetime, timedelta

class GlobalTime:
    def __init__(self, start_hour=5, start_minute=30):
        self.start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
        self.current_time = self.start_time
    
    def update_time(self):
        self.current_time = datetime.now()
    
    def get_elapsed_time(self):
        return self.current_time - self.start_time
    
    def get_current_time(self):
        return self.current_time