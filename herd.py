from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
        

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('Rex', 20))
        self.dinosaurs.append(Dinosaur('Vic', 20))
        self.dinosaurs.append(Dinosaur('Big Ben', 20))

        
      
