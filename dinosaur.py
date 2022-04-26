class Dinosaur:
    def __init__(self, name):
        self.name = 'Rex'
        self.attack_power = 10
        self.health = 100
    
    def dino_when_it_attacks(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power 
       
    def dino_attack(self, robot):
        self.attack_power -= robot 

 