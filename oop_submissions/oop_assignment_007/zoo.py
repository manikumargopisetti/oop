class Deer:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(age_in_months))
            
        if required_food_in_kgs <= 0:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(required_food_in_kgs))
        
        self._age_in_months = age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property 
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs+=2
        self._age_in_months+=1
        
    def make_sound(self):
        print("Buck Buck")
        
    def breathe(self):
        print("Breathe in air")
    def hunt(self):
        pass
        
class Lion(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

    def grow(self):
        self._required_food_in_kgs+=4
        self._age_in_months+=1
        
    def make_sound(self):
        print("Roar Roar")
        
class Shark(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

    def grow(self):
        self._required_food_in_kgs+=8
        self._age_in_months+=1
        
    def make_sound(self):
        print("Shark Sound")
        
    def breathe(self):
        print("Breathe oxygen from water")

class GoldFish(Shark):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

    def grow(self):
        self._required_food_in_kgs+=0.2
        self._age_in_months+=1
        
    def make_sound(self):
        print("Hum Hum")
        
class Snake(Deer):
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    
    def grow(self):
        self._required_food_in_kgs+=0.5
        self._age_in_months+=1
    
    def make_sound(self):
        print("Hiss Hiss")
        
class Zoo:
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self.li=[]
    @property 
    def reserved_food_in_kgs(self):
        self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def add_animal(self,animal):
        self.li.append(animal)
        
    def count_animals(self):
        return len(self.li)
        