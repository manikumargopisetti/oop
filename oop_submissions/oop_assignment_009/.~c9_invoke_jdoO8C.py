class Pokemon:
    sound = ""
    running = ""
    def __init__(self,name,level):
        if name == "":
            raise ValueError('name cannot be empty')
        if level < 0:
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
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("Air attack with 10 damage")
        if self.level > 1:
            x = self._level * 5
            print("Air attack with {} damage".format(x))    
class Swanna(Pokemon):
    sound = "Swanna...Swanna"
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)
    def attack(self):
        if self._level == 1:
            print("water attack with 9 damage")
            print("Air attack with 5 damage")
        if self._level > 1:
            x = self._level * 9
            y = self._level * 5
            print("water attack with {} damage".format(x))
            print("Air attack with {} damage".format(y))
class Zapdos(Pokemon):
    sound = "Zap...Zap"
    
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