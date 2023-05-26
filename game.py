import random
import welcome
from classes import Hero, Game, DoctorOctopus, Electro, Mysterio, GreenGoblin

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
    
    print(welcome)
    
    for enemy in enemies:
        print(f"You have encountered {enemy.name}. Get ready to fight!")
        answer = input("Are you ready to accept the challenge? (yes or no) ")
        if answer.lower() == "yes":
            games.new_round()
            prefight(hero, enemy)
            fight(hero, enemy)
            print(f"Your health = {hero.health} {enemy.name} health = {enemy.health}")
            if not hero.alive():
                break
        else:
            print("You have lost the game.")
            break
            
    if hero.alive():
        print("Congratulations! You have saved Queens from the Villians reign of terror!")
if __name__ == "__main__":
    main()

