import random 


from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        
        

    def display_welcome(self):
        print('Welcome to the ASTROWORLD! Where Winners Live and Losers Die!')

    def battle(self):
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        self.herd.dinosaurs[0].attack(self.fleet.robots[0])

    # def dino_turn(self, dinosaur):
    #     pass

    # def robo_turn(self, robot):
    #     pass

    # def show_dino_opponent_options(self):
    #     pass

    # def show_robo_opponent_options(self):
    #     pass

    # def display_winners(self):
    #     pass 

    