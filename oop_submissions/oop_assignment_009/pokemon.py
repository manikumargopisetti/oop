class Pokemon:
    sound = ""
    running = ""
    flying = ""
    swimming = ""
    def __init__(self,name,level):
        if name == "":
            raise ValueError('name cannot be empty')
        if level <= 0:
            raise ValueError('level should be > 0')
        self._name = name 
        self._level = level
    @property 
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def run(cls):
        print(cls.running)
    @classmethod 
    def fly(cls):
        print(cls.flying)
    @classmethod
    def swim(cls):
        print(cls.swimming)
        
class Pikachu(Pokemon):
    sound = "Pika Pika"
    running = "Pikachu running..."
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("Electric attack with 10 damage")
        if self.level > 1:
            x = self._level * 10
            print("Electric attack with {} damage".format(x))
class Squirtle(Pokemon):
    sound = "Squirtle...Squirtle"
    running = "Squirtle running..."
    swimming ="Squirtle swimming..."
    
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("Water attack with 9 damage")
        if self.level > 1:
            x = self._level * 9
            print("Water attack with {} damage".format(x))    
class Pidgey(Pokemon):
    sound = "Pidgey...Pidgey"
    flying = "Pidgey flying..."
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("Air attack with 5 damage")
        if self.level > 1:
            x = self._level * 5
            print("Air attack with {} damage".format(x))    
class Swanna(Pokemon):
    sound = "Swanna...Swanna"
    flying = "Swanna flying..."
    swimming = "Swanna swimming..."
    
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("Water attack with 9 damage")
            print("Air attack with 5 damage")
        if self._level > 1:
            x = self._level * 9
            y = self._level * 5
            print("Water attack with {} damage".format(x))
            print("Air attack with {} damage".format(y))
class Zapdos(Pokemon):
    sound = "Zap...Zap"
    flying = "Zapdos flying..."
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("Electric attack with 10 damage")
            print("Air attack with 5 damage")
        if self.level > 1:
            x = self._level * 10
            y = self._level * 5
            print("Electric attack with {} damage".format(x))
            print("Air attack with {} damage".format(y))    
class Island:
    total_poke_list = []
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.total_poke_list.append(self)
    @property 
    def name(self):
        return self._name
    @property  
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property     
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property 
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self.name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
    
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
        else:
            print("Island at its max pokemon capacity")
    @classmethod        
    def get_all_islands(cls):
        return cls.total_poke_list

class Trainer:
    def __init__(self,name,experience=100):
        self._name = name
        self._experience = experience
        self._max_food_in_bag = experience *10
        self._food_in_bag = 0
        self._current_island=None
        self.li=[]

    @property 
    def name(self):
        return self._name
    @property 
    def experience(self):
        return self._experience
    @property 
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property 
    def food_in_bag(self):
        return self._food_in_bag
    def __str__(self):
        return '{}'.format(self._name)
    def move_to_island(self,island):
        self._current_island=island
    @property
    def current_island(self):
        if self._current_island == None:
            print("You are not on any island")
            return
        
        return self._current_island
        
    def collect_food(self):
        if self._current_island==None:
            print('Move to an island to collect food')
        else:
            if self._current_island._total_food_available_in_kgs < self._max_food_in_bag:
                self._food_in_bag = self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs=0
            elif self._food_in_bag < self._max_food_in_bag:
                self._current_island._total_food_available_in_kgs -= self._max_food_in_bag
                self._food_in_bag = self._max_food_in_bag
                
    def catch(self,pokemon):
        if self._experience >= 100 * pokemon._level:
            self.li.append(pokemon)
            print(f'You caught {pokemon.name}')
            self._experience +=20*pokemon._level
            pokemon._master=self
            return
        print(f'You need more experience to catch {pokemon.name}')
        
    def get_my_pokemon(self):
        return self.li
    pass
