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
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"\n***   Round: {self.round}   ***\n")  


def prefight(hero, enemy): 
    print(f"{hero.name} vs {enemy.name}") 
    print(f"{hero.name} - Health: {hero.health} Attack: {hero.attack}") 
    print(f"{enemy.name} - Health: {enemy.health} Attack: {enemy.attack}")

def fight(hero, enemy):
    while hero.alive() and enemy.alive():
        choice = input("Attack, Defend, Heal")
        if choice == "quit":
            break
        if choice == "Defend":
            hero.block(enemy)
        if choice == "Heal":
            hero.pizza()
        if choice == "Attack":
            hero.attack_enemy(enemy)
        if not enemy.alive():
            break
    
        enemy.attack_enemy(hero)
        print(f"{hero.name} - Health: {hero.health}")
        print(f"{enemy.name} - Health: {enemy.health}")
        if not hero.alive():
            break
            
    if hero.alive():
        print(f"{hero.name} defeated {enemy.name}!")
        return True
    else:
        print(f"{hero.name} was defeated by {enemy.name}. Game over!")
        return False

games = Game()

def main():
    hero = Hero("Spider-Man", 30, 10000, 1000)
    enemies = [DoctorOctopus(), Electro(), Mysterio(), GreenGoblin()]
    
    print("Welcome to Queens! Your mission is to defeat all the enemies and save the city.")
    
    for enemy in enemies:
        print(f"You have encountered {enemy.name}. Get ready to battle!")
        answer = input("Are you ready to accept your next challenge? (yes or no) ")
        if answer.lower() == "yes":
            games.new_round()
            prefight(hero, enemy)
            fight(hero, enemy)
            print(f"Your health = {hero.health} {enemy.name} health = {enemy.health}")
            if not hero.alive():
                break
        else:
            print("Sorry, you have lost the game.")
            break
            
    if hero.alive():
        print("Congratulations! You have saved Queens from the villians reign of terror!")
if __name__ == "__main__":
    main()

