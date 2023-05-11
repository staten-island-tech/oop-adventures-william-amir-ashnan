class player:
    def __init__(self, name):
        self.name = name
        self.attack = 500
        self.health = 1000

class NPC(player):
    def __init__(self, name, attack, health):
        super().__init__(name)
        self.name = name
        self.attack = attack
        self.health = health
    def __str__(self):
        return f"{self.name}, {self.attack}, {self.health}"

DoctorOctopus = NPC("Doctor Octopus", "15", "125" )
Electro = NPC("Electro", "20", "150")
Mysterio = NPC("Mysterio", "25", "175")
GreenGoblin = NPC("Green Goblin", "40", "175")

print(NPC)