from weapon import Weapon



class Robot:
    def __init__(self):
        self.name = 'Optimist'
        self.health = 100
        self.weapon = Weapon("lazer", 10) 
  
        
    def robot_display(self, name):
        self.name = name
        
        
    def robot_when_it_gets_attacked(self, health):
       self.health -= health 
       

