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
    pass

class DoctorOctopus(Enemy):
    def __init__(self):
        super().__init__("Doctor Octopus", random.randint(10,20), 125)
        
class Electro(Enemy):
    def __init__(self):
        super().__init__("Electro", random.randint(20,25),150)
        
class Mysterio(Enemy):
    def __init__(self):
        super().__init__("Mysterio", random.randint(25,30), 175)

class GreenGoblin(Enemy):
    def __init__(self):
        super().__init__("Green Goblin", random.randint(30,40), 200)

class Game:
    def __init__(self):
        self.game_over = False
        self.challenge = 0

    def new_round(self):
        self.challenge += 1
        print(f"\n***   Enemy: {self.challenge}   ***\n")  