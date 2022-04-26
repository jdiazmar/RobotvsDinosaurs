from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
        

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('Rex'))
        self.dinosaurs.append(Dinosaur('Vic'))
        self.dinosaurs.append(Dinosaur('Big Ben'))
      
