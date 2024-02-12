#
class Superhero():
    # def __init__(self, superhero_name, superhero_identity, superhero_power, superhero_enemy, superhero_lair):
    def __init__(self, superhero_name, superhero_identity, superhero_power, superhero_enemy):
        self.name = superhero_name
        self.identity = superhero_identity
        self.power = superhero_power
        self.enemy = superhero_enemy
       # self.lair = superhero_lair

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, my name is {self.identity}, my enmy is {self.enemy}")

    def name_length(self):
        print(len(self.name))

    ## setters
        
    # def set_lair(self, lair):
    #     self.lair = lair

    def get_power(self):
        return self.power
    