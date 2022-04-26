from weapon import Weapon



class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Laser', 10) 
  
        
    def robot_display(self, name):
        self.name = name

    def attack(self, dino):
        dino.health -= self.weapon.attack_power 
        
        
    def robot_when_it_gets_attacked(self, health):
       self.health -= health 
       

