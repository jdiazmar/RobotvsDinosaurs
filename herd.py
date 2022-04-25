from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs = [Dinosaur.name, Dinosaur.health, Dinosaur.attack_power]