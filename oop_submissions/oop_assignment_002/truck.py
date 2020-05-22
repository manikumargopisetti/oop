from car import Car
class Truck(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        if max_cargo_weight < 0:
            raise ValueError('Invalid value for cargo_weight')
        self.Trk_load=0
        self._max_cargo_weight=max_cargo_weight
        self.is_engine_started
        
    def start_engine(self):
        self.is_engine_started =True
        
    def load(self):
        #if 
        pass
    def unload(self):
        pass