class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def __str__(self) -> str:
        return f'Using a {self.name}'

        
