
class Character:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health
        
    def alive(self):
        return self.health > 0
        
    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} attacked {enemy.name} for {self.attack} damage.")
        
class Hero(Character):
    def __init__(self, name, attack, health, heal):
        super().__init__(name, attack, health)
        self.heal = heal
        
    def use_pizza(self):
        self.health += self.heal
        print(f"{self.name} ate a slice of pizza and regained {self.heal} health.")
        
    def power_up(self):
        self.attack = 40
        self.health = 175
        print(f"{self.name} powered up and increased their attack to {self.attack} and health to {self.health}.")
        
class Enemy(Character):
    pass

class DoctorOctopus(Enemy):
    def __init__(self):
        super().__init__("Doctor Octopus", 15, 125)
        
class Electro(Enemy):
    def __init__(self):
        super().__init__("Electro", 20, 150)
        
class Mysterio(Enemy):
    def __init__(self):
        super().__init__("Mysterio", 25, 175)

class GreenGoblin(Enemy):
    def __init__(self):
        super().__init__("Green Goblin", 40, 200)

def prefight(hero, enemy): 
    print(f"{hero.name} vs {enemy.name}") 
    print(f"{hero.name} - Health: {hero.health} Attack: {hero.attack}") 
    print(f"{enemy.name} - Health: {enemy.health} Attack: {enemy.attack}")

def fight(hero, enemy):
    while hero.alive() and enemy.alive():
        # Hero attacks first
        hero.attack_enemy(enemy)
        if not enemy.alive():
            break
            
        # Enemy attacks
        enemy.attack_enemy(hero)
        if not hero.alive():
            break
            
    if hero.alive():
        print(f"{hero.name} defeated {enemy.name}!")
        return True
    else:
        print(f"{hero.name} was defeated by {enemy.name}. Game over!")
        return False

def main():
    hero = Hero("Spider-Man", 30, 150, 25)
    enemies = [DoctorOctopus(), Electro(), Mysterio(), GreenGoblin()]
    
    print("Welcome to Queens! Your mission is to defeat all the enemies and save the city.")
    
    for enemy in enemies:
        print(f"You have encountered {enemy.name}. Get ready to fight!")
        answer = input("Are you ready to accept the challenge? (yes or no) ")
        if answer.lower() == "yes":
            fight(hero, enemy)
            if not hero.alive():
                break
        else:
            print("You have lost the game.")
            break
            
    if hero.alive():
        print("Congratulations! You have saved Queens from the Green Goblin's reign of terror!")
if __name__ == "__main__":
    main()

