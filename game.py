import moveclasses 
import npcclasses 

class Game:
    def __init__(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"\n***   Round: {self.round}   ***\n")  

    # Check if either or both Players is below zero health
    def check_win(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            self.game_over = True
            print("You Lose")
        elif opponent.health < 1 and player.health > 0:
            self.game_over = True
            print("You Win")
        elif player.health < 1 and ai.health < 1:
            self.game_over = True
            print("*** Draw ***")


    def display_result(self, player, opponent):
            print(f"{player.name} used a {player.attack.name}, {opponent.name} used a {opponent.defend.name} Shield\n")
            print(f"{player.name} caused damage to {opponent.name}\n")

    def take_turn(self, player, opponent):

        if player.weapon not in opponent.defend.blocks:
            opponent.damage()
            current_game.display_result(player, opponent)
        else:
            print(f"{player.name} used a {player.attack.name}, {opponent.name} used a {opponent.defend.name} Shield\n")
            print(f"{opponent.name} blocked {player.name}'s attack - No Damage")

# Setup Game Objects
current_game = Game()
human = player("Mark")
ai = NPC("Computer")

players = [human, ai]

# Main Game Loop
while not current_game.game_over:
    for player in players:
        player.select_weapon()
        player.select_shield()
    current_game.new_round()
    current_game.take_turn(human, ai)
    current_game.take_turn(ai, human)
    print(f"{human.name}'s health = {human.health}")
    print(f"{ai.name}'s health = {ai.health}")
    current_game.check_win(human, ai)