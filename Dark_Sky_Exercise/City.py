class City:
    
    def __init__(self, city_ref, lat, lon):
        
        self.city_reference = city_ref
        self.latitude = lat
        self.longitude = lon
        self.five_day_minmax = []
    
    def add_minmax(self, min, max):
        
        day_temp_min_max = { "min" : float(min), "max" : float(max)}
        
        self.five_day_minmax.append(day_temp_min_max)
        
    def get_min_avg(self):
        
        n = len(self.five_day_minmax)
        total = 0
        
        for i in range(n):
            day = self.five_day_minmax[i]
            total += day[ "min" ]
        
        return round( total / n, 2 )
        
    def get_max_avg(self):
        
        n = len(self.five_day_minmax)
        total = 0
        
        for i in range(n):
            day = self.five_day_minmax[i]
            total += day[ "max" ]
        
        return round( total / n, 2 )    
    
    def get_5d_minmax(self):
        return self.five_day_minmax
        
    def get_lat(self): 
        return self.latitude
    
    def get_lon(self):
        return self.longitude
    
    def get_city_ref(self):
        return self.city_reference