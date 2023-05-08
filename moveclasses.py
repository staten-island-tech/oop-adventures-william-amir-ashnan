class move:
    def __init__(self, name):
        self.name=name 

class attack(move):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
    def __str__(self):
        return f"{self.name}, {self.damage}"

class defend(move):
    def __init__(self, name, block):
        super().__init__(name)
        self.block = block
        return f"{self.name}, {self.block}"

class heal(move):
    def __init__(self, name, eat):
        super().__init__(name)
        self.eat = eat
        return f"{self.name}, {self.eat}"
        