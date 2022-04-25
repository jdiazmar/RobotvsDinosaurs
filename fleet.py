from robot import Robot


class Fleet:
    def __init__(self):
        self.robot = []

    
    def create_fleet(self, robot_attributes):
        self.robot = [Robot.name, Robot.health, Robot.weapon]      