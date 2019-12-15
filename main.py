from cards import *
from game import *
import time

playerlist = []
current_player = []
turn_count = 0

if input("Welcome to Dominion Bot, would you like to start a game? ") == 'yes':
    player_no = int(input("How many players?: "))
    game = Game(player_no)
    for x in range(player_no):
        x = Player(x + 1)
        playerlist.append(x)
    game.startgame(game, playerlist)
else:
    print("Why are you here then lol")

while True: #Game loop!

    current_player.append(playerlist[0])
    playerlist = playerlist[1:]
    current_player = current_player[0]
    current_player.play = True
    current_player.prop_check(game)

    print('\nPlayer', current_player.number)
    print('Turn', current_player.turn_count)

    while current_player.play == True: #Turn loop
        game.info(current_player, game, playerlist)
        try:
            command = input('What would you like to do? ')
            game.command_list[command](current_player, game, playerlist) 
            game.check_end(game, playerlist, current_player)
        except SystemExit:
            sys.exit()
        except Exception as e:
            raise
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # print(e.args, exc_tb.tb_lineno)
            pass
    current_player.end_turn(game)
    playerlist.append(current_player)
    current_player = []
    
    




