from weapon import Weapon



class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon() 
  
        
    def robot_display(self, name):
        self.name = name
        
        
    def robot_when_it_gets_attacked(self, health):
       self.health -= health 
       

