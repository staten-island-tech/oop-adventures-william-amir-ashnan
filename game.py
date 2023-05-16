from npcclasses import SpiderMan, DoctorOctopus, Electro, Mysterio, GreenGoblin
def prefight(hero, enemy): 
    print(f"{hero.name} vs {enemy.name}") 
    print(f"{hero.name} - Health: {hero.health} Attack: {hero.attack}") 
    print(f"{enemy.name} - Health: {enemy.health} Attack: {enemy.attack}")

def fight(hero, enemy):
    while hero.alive() and enemy.alive():
        # Hero attacks first
        hero.attack_enemy(enemy)
        print(f"Your health = {hero.health} {enemy.name} health = {enemy.health}")
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
    hero = SpiderMan("Spider-Man", 30, 150, 25)
    enemies = [DoctorOctopus(), Electro(), Mysterio(), GreenGoblin()]
    
    print("Welcome to Queens! Your mission is to defeat all the enemies and save the city.")
    
    for enemy in enemies:
        print(f"You have encountered {enemy.name}. Get ready to fight!")
        answer = input("Are you ready to accept the challenge? (yes or no) ")
        if answer.lower() == "yes":
            prefight(hero, enemy)
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

