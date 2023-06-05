import random
class Character:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def block(self, enemy):
        self.health += enemy.attack
        print(f"{self.name} blocked {enemy.name} for {enemy.attack} damage")
    
    def alive(self):
        return self.health > 0
        
    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} attacked {enemy.name} for {self.attack} damage.")
        
class Hero(Character):
    def __init__(self, name, attack, health, heal):
        super().__init__(name, attack, health)
        self.heal = heal
    
    def quit(self):
        self.health -= self.health
        
    def pizza(self):
        self.health += self.heal
        print(f"{self.name} ate a slice of pizza and regained {self.heal} health.")
        
class Enemy(Character):
    def __init__(self, name, attack, health):
        super().__init__(name, attack, health)

Tutorialbot = Enemy("Tutorial Bot", random.randint(10,15), 100)

DoctorOctopus = Enemy("Doctor Octopus", random.randint(10,20), 125)
        
Electro = Enemy("Electro", random.randint(20,25),150)
        
Mysterio= Enemy("Mysterio", random.randint(25,30), 175)

GreenGoblin = Enemy("Green Goblin", random.randint(30,40), 200)

