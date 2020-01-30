
from datetime import datetime


class Cache:
    def __init__(self,name,coord):
        super().__init__()
        self.name = name
        self.cache = {}
        self.coord = coord

    def empty(self):
        return self.cache == {}

    def add(self, value):
        time = datetime.now().isoformat()
        if value not in self.cache:
            self.cache[value] = {'date_time' : time}

    def remove(self):
        previous = None
        for val in self.cache:
            if previous is None:
                previous = val
            elif self.cache[val]['date_time'] < self.cache[previous]['date_time']:
                previous = val
        self.cache.pop(previous)

    def print(self):
        return self.cache
    

    


        
