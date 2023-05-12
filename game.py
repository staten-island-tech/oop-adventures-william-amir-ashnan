from moveclasses import move, attack, defend, heal
from npcclasses import player, NPC 

class Game:
    def __init__(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"\n***   Round: {self.round}   ***\n")  

    # Check if either or both Players is below zero health
    def check_win(self, player, NPC):
        if player.health < 1 and NPC.health > 0:
            self.game_over = True
            print("You Lose")
        elif NPC.health < 1 and player.health > 0:
            self.game_over = True
            print("You Win")
        elif player.health < 1 and ai.health < 1:
            self.game_over = True
            print("*** Draw ***")


    def display_result(self, player, NPC):
            print(f"{player.name} used a {player.attack.name}, {NPC.name} used a {NPC.defend.name} Shield\n")
            print(f"{player.name} caused damage to {NPC.name}\n")

    def take_turn(self, player, NPC):

        if player.weapon not in NPC.defend.blocks:
            NPC.damage()
            current_game.display_result(player, NPC)
        else:
            print(f"{player.name} used a {player.attack.name}, {NPC.name} used a {NPC.defend.name} Shield\n")
            print(f"{NPC.name} blocked {player.name}'s attack - No Damage")

# Setup Game Objects
current_game = Game()
human = player("You")
ai = NPC("Computer")

players = [human, ai]

# Main Game Loop
while not current_game.game_over:
    current_game.new_round()
    current_game.take_turn(human, ai)
    current_game.take_turn(ai, human)
    print(f"{human.name}'s health = {human.health}")
    print(f"{ai.name}'s health = {ai.health}")
    current_game.check_win(human, ai)