import random 


from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        random.choice(Fleet.create_fleet, Herd.create_herd)
        

    def display_welcome(self):
        self.display_welcome = 'Welcome to the ASTROWORLD! Where Winners Live and Losers Die!'

    # def battle(self):
    #     pass

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

    