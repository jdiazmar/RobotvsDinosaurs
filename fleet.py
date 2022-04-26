from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
        

    
    def create_fleet(self):
       self.robots.append(Robot('Optimus'))
       self.robots.append(Robot("Waldo"))
       self.robots.append(Robot('Gary'))


