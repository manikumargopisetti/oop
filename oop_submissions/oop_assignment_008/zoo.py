class Animals:
    sound=""
    food_increse = 0
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months !=1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(age_in_months))
        if required_food_in_kgs <= 0:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(required_food_in_kgs))
        self._age_in_months= age_in_months
        self._breed= breed
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
    
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
    
    def grow(self):
        self._required_food_in_kgs += self.food_increse
        self._age_in_months += 1
        
class LandAnimals: 
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
class WaterAnimals:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
    
class HuntLandAnimals:
    def hunt(self,zoo_parks):
        c=0
        for i in zoo_parks.li:
            if i.__class__ == Deer:
                zoo_parks.li.remove(i)
                c+=1
        if c==0:
            print("No deers to hunt")
                
class HuntWaterAnimals:
    def hunt(self,zoo_parks):
        c = 0
        for j in zoo_parks.li:
            if j.__class__== GoldFish:
                zoo_parks.li.remove(j)
                c+=1
        if c == 0:
            print("No GoldFish to hunt")
    
class Deer(Animals,LandAnimals):
    sound = "Buck Buck"
    food_increse=2
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
    
class Lion(Animals,LandAnimals,HuntLandAnimals):
    sound = "Roar Roar"
    food_increse=4
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

class Shark(Animals,WaterAnimals,HuntWaterAnimals):
    sound = "Shark Sound"
    food_increse=8
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

class GoldFish(Animals,WaterAnimals):
    sound = "Hum Hum"
    food_increse=0.2
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

class Snake(Animals,LandAnimals,HuntLandAnimals):
    sound = "Hiss Hiss"
    food_increse=0.5
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)

class Zoo:
    total_animals_in_all_zoos=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs   
        self.li=[]
    @property 
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def add_animal(self,animal):
        self.li.append(animal)
        self.total_animals_in_all_zoos.append(animal)
        
    def count_animals(self):
        return len(self.li)
        
    def feed(self,animal):
        feed_req =animal._required_food_in_kgs
        if self._reserved_food_in_kgs > feed_req:
            animal.grow()
            self._reserved_food_in_kgs -= feed_req
            
    @staticmethod
    def count_animals_in_given_zoos(zoo):
        c=0
        for i in zoo:
            c+=i.count_animals()
        return c
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.total_animals_in_all_zoos)