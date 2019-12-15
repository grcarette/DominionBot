# Artisan Bandit Bureaucrat Cellar Chapel Council_Room Festival Gardens Harbinger Laboratory  

from cards import *
import random, math, sys, time
from itertools import combinations


deck = []
class Game:
    def __init__(self, players):
        self.cardlist = [str(x) for x in input("Enter 10 cards: ").split()]
        self.players = players
        self.deck_index = {}
        self.command_list = {
            'buy' : self.purchase,
            'viewcards' : self.viewcards,
            'info' : self.info,
            'endturn' : self.endturn,
            'help' : self.help,
            'stop' : self.stop,
            'code' : self.code,
            'action' : self.action,
            'emptydeck' : self.emptydeck,
            'addcard' : self.addcard,
            'cheat' : self.cheat,
            'devinfo': self.devinfo,
            'printcoun' : self.printcoun,
            'discard' : self.discard
            }
        self.value_spent = 0
        self.buys_used = 0
        self.actions_used = 0

        self.value_added = 0
        self.buys_added = 0
        self.actions_added = 0

        self.trash_list = []
        self.empty_decks = 0

    def startgame(self, game, Plist):
        index = 0
        for card in game.cardlist:
            current_list = []
            for y in range (10):
                current_list.append(card_list[card][0]())
            self.deck_index[index] = [card, current_list]
            index += 1
            current_list = []

        ##Creating Default Decks!!!
        
        if self.players < 3:
            card_no = 8
        else: 
            card_no = 12
        current_list = []
        for x in range(card_no):
            current_list.append(Estate())
        self.deck_index[index] = ['Estate', current_list]
        index += 1
        current_list = []
        for x in range(card_no):
            current_list.append(Duchy())
        self.deck_index[index] = ['Duchy', current_list]
        index += 1
        current_list = []
        for x in range(card_no):
            current_list.append(Province())
        self.deck_index[index] = ['Province', current_list]
        index += 1
        current_list = []
        for x in range(10 * (self.players - 1)):
            current_list.append(Curse())
        self.deck_index[index] = ['Curse', current_list]
        index += 1
        current_list = []
        for x in range(60 - 2*self.players):
            current_list.append(Copper())
        self.deck_index[index] = ['Copper', current_list]
        index += 1
        current_list = []
        for x in range(60 - 2*self.players):
            current_list.append(Silver())
        self.deck_index[index] = ['Silver', current_list]
        index += 1
        current_list = []
        for x in range(60 - 2*self.players):
            current_list.append(Gold())
        self.deck_index[index] = ['Gold', current_list]


    def purchase(self, Player, game, Plist):
        if Player.buys > 0:
            print(Player.buys)
            cardno = int(input("Which card do you want to buy? "))
            try:
                if Player.value >= game.deck_index[cardno][1][0].cost:
                    if Player.take_card(cardno, game, Player.discard) == True:
                        self.buys_used += 1
                        self.value_spent += game.deck_index[cardno][1][0].cost
                        Player.prop_check(game)
                        pass
                    else:
                        self.purchase(Player, game, Plist)
                elif cardno == "none":
                    pass
                else:
                    print("You don't have enough money! ")
                    self.purchase(Player, game, Plist)
            except IndexError:
                print("There aren't any left!")
                self.purchase(Player, game. Plist)
        else: 
            print("You don't have any buys left!")

    def viewcards(self, Player, game, Plist):
        for x in range(len(self.deck_index)):
            print(x,'',self.deck_index[x][0], ' : ' ,len(self.deck_index[x][1]))
            print('     ', 'cost : ', card_list[self.deck_index[x][0]][1]) 
        print(self.trash_list)

    def help(self, Player, game, Plist):
        print('')
        print('COMMANDS:')
        print('buy : Purchase a card')
        print('action : Use an action card')
        print('endturn : end turn')
        print('viewcards : view cards remaining in game decks')
        print('info : view information about your current turn')
        print('stop : stop program')
        print('')

    def endturn(self, Player, game, Plist):
            Player.play = False

    def info(self, Player, game, Plist):

        templist = []
        for x in range(len(Player.hand)):
            templist.extend([str(x) + ' : ' + Player.hand[x].name])
        print('\nCurrent Hand : ', templist)
        print('Actions Remaining : ', Player.actions)
        print('Buys Remaining : ', Player.buys)
        print('Value of hand : ', Player.value)
        print('Value spent : ', self.value_spent, '\n')
        # print('you currently have : ', sum([x.pvic for x in Player.hand + Player.deck + Player.discard]), 'points')
        # print('DISCARD')
        # print([y.name for y in Player.discard])
        # print('DECK')
        # print([y.name for y in Player.deck])

    def devinfo(self, Player, game, Plist):
        print('')
        for x in Plist:
            print(x.number)
            print('HAND')
            print([y.name for y in x.hand])
            print('DISCARD')
            print([y.name for y in x.discard])
            print('DECK')
            print([y.name for y in x.deck])
        print('')

    def stop(self, Player, game, Plist):
        sys.exit()

    def code(self, Player, game, Plist):
        eval(input('Input Code'))

    def emptydeck(self, Player, game, Plist):
        deckchoice = int(input("Which deck would you like to erase? "))
        self.deck_index[deckchoice][1] = []

    def addcard(self, Player, game, Plist):
        cardchoice = input("Which card would you like to add? ")
        playerchoice = int(input("To which player?" ))
        if playerchoice == Player.number:
            Player.hand.append(card_list[cardchoice][0]())
        else:
            for Other in Plist:
                if playerchoice == Other.number:
                    Other.hand.append(card_list[cardchoice][0]())
        Player.prop_check(game)

    def cheat(self, Player, game, Plist):
        cheat_no = int(input("How many? "))
        self.value_added += cheat_no
        self.buys_added += cheat_no
        self.actions_added += cheat_no
        Player.prop_check(game)

    def action(self, Player, game, Plist):
        has_action = False
        if Player.actions > 0:
            for Card in Player.hand:
                if Card.type == 'Action':
                    has_action = True
            if has_action == True: 
                templist = []
                for x in range(len(Player.hand)):
                    templist.extend([str(x) + ' : ' + Player.hand[x].name])
                print('Current Hand : ', templist)
                choice = int(input("Which card would you like to use? "))
                if Player.hand[choice].used == False:
                    active_card = Player.hand[choice]
                    active_card.action(Player, game, game.reaction_check(Player, game, Plist))
                    game.actions_used += 1
                    self.buys_added += active_card.pbuy
                    self.actions_added += active_card.pact
                    Player.draw(active_card.pcar)
                    Player.prop_check(game)
                else:
                    print('You have already used this card!')
            else:
                print("You don't have any action cards! ")
        else: 
            print('You dont have any actions left dummy!')

    def endgame(self, Plist):
        print('GAME OVER!!')
        for Player in Plist:
            fulldeck = Player.hand + Player.deck + Player.discard
            for y in fulldeck:
                try:
                    y.game_end(Player, fulldeck)
                except AttributeError:
                    pass
            Player.points = sum([x.pvic for x in fulldeck])
        Plist.sort(key=lambda x: x.points, reverse=True)
        for Player in Plist:
            print("Player",Player.number, 'Finished with:', Player.points, "points")
        print('Player', Plist[0].number, "is the winner!!")
        sys.exit()

    def printcoun(self, game, playerlist, current_player):
        print('e')
        print(self.deck_index[5][1])
        
    def check_end(self, game, playerlist, current_player):
        empty_decks = 0
        for x in game.deck_index:
            if len(game.deck_index.get(x)[1]) == 0:
                empty_decks += 1
        if game.empty_decks < empty_decks:
            game.empty_decks += 1
            print("There are now", game.empty_decks, "empty decks!")
        if empty_decks == 3:
            playerlist.append(current_player)
            game.endgame(playerlist)
        return empty_decks

    def curse(self, playerlist, game):
        for Other in playerlist:
            Other.takecard(13, game, Other.discard)

    def trash(self, card, fromlist):
        self.trash_list.append(card)
        fromlist.remove(card)

    def discard(self, Player, game, Plist):
        templist = []
        for x in range(len(Player.hand)):
            templist.extend([x, Player.hand[x].name])
        print(templist)

        discard = [int(x) for x in input("Which cards would you like to discard? ").split()]
        discard.sort(reverse = True)
        for x in discard:
            Player.discard_card(x)
    
    def reaction_check(self, Player, game, Plist):
        endlist = []
        for Other in Plist:
            react_list = []
            for card in range(len(Other.hand)):
                if Other.hand[card].subtype == 'Reaction':
                    if Other.hand[card].reaction_conditions(Player, game, Plist) == True and Other.hand[card].reaction_used == False:
                        react_list.append(str(card) + ' : ' + Other.hand[card].name)
            if len(react_list) == 0:
                endlist.append(Other)
            if len(react_list) > 0:
                print(react_list)
                choice = input('Which reaction would you like to use? "None" to exit ')
                if str(choice).lower() == 'none':
                    endlist.append(Other)
                else:
                    Other.hand[int(choice)].reaction_used = True
        return endlist

    def index_list(self, deck):
        templist = []
        for card in range(len(deck)):
            templist.append(str(card) + ': ' + deck[card].name)
        print(templist)




                

class Player:
    def __init__(self, no):
        self.discard = []
        self.deck = []
        self.hand = []
        self.turn_count = 0
        self.actions = 0
        self.buys = 0
        self.value = 0
        self.points = 0
        self.play = False
        for x in range(7):
            self.deck.append(Copper())
        for x in range(3):
            self.deck.append(Estate())
        random.shuffle(self.deck)
        self.hand.extend(self.deck[:5])
        self.deck = self.deck[5:]
        self.number = no

    def prop_check(self, game):
        value = sum(x.pval for x in self.hand)
        self.actions = 1 - game.actions_used + game.actions_added ##add in actions when actions are used
        self.buys = 1 - game.buys_used + game.buys_added ##add in buys added when actions are used
        self.value = value - game.value_spent + game.value_added
        return self.actions, self.buys, self.value

    def end_turn(self, game):
        self.turn_count += 1

        game.buys_used = 0
        game.value_spent = 0
        game.actions_used = 0

        game.buys_added = 0
        game.value_added = 0
        game.actions_added = 0

        self.discard.extend(self.hand)
        self.hand = []
        self.actions = 1
        self.buys = 1
        if len(self.deck) < 5:
            random.shuffle(self.discard)
            for x in self.discard:
                x.__init__()
            self.deck.extend(self.discard)
            self.discard = []

            self.hand = self.deck[:5]
            self.deck = self.deck[5:]
        else: 
            self.hand = self.deck[:5]
            self.deck = self.deck[5:]

    def take_card(self, cardno, game, tolist):
        cardsleft = len(game.deck_index[cardno][1])
        if cardsleft == 0:
            print("There aren't any ",game.deck_index[cardno][0],"'s left! ")
            return False
        else:
            tolist.append(game.deck_index[cardno][1][0])
            game.deck_index[cardno][1] = game.deck_index[cardno][1][1:]
            return True

    def draw(self, no):
        if len(self.deck) < no:
            random.shuffle(self.discard)
            for x in self.discard:
                x.__init__()
            self.deck.extend(self.discard)
            self.discard = []

        self.hand.extend(self.deck[:no])
        self.deck = self.deck[no:]

    def discard_card(self, no):
        self.discard.append(self.hand[no])
        self.hand.remove(self.hand[no])

    def reveal(self, no):
        revealed_cards = []
        if len(self.deck) < no:
            random.shuffle(self.discard)
            for x in self.discard:
                x.__init__()
            self.deck.extend(self.discard)
            self.discard = []
        revealed_cards.extend(self.deck[:no])
        self.deck = self.deck[no:]
        return revealed_cards






        