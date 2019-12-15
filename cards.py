##pval is no longer included in init! include in action since the value doesnt exist unless action is used

import math
import threading
import time

class Copper: 
    def __init__(self):
        self.pval = 1
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 0
        self.name = 'Copper'
        self.type = 'Treasure'
        self.subtype = 'None'

class Silver: 
    def __init__(self):
        self.pval = 2
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 3
        self.name = 'Silver'
        self.type = 'Treasure'
        self.subtype = 'None'

class Gold: 
    def __init__(self):
        self.pval = 3
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 6
        self.name = 'Gold'
        self.type = 'Treasure'
        self.subtype = 'None'

class Estate: 
    def __init__(self):
        self.pval = 0
        self.pvic = 1
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Estate'
        self.type = 'Victory'
        self.subtype = 'None'

class Duchy: 
    def __init__(self):
        self.pval = 0
        self.pvic = 3
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Duchy'
        self.type = 'Victory'
        self.subtype = 'None'

class Province: 
    def __init__(self):
        self.pval = 0
        self.pvic = 6
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 8
        self.name = 'Province'
        self.type = 'Victory'
        self.subtype = 'None'

class Curse: 
    def __init__(self):
        self.pval = 0
        self.pvic = -1
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 0
        self.name = 'Curse'
        self.type = 'Victory'
        self.subtype = 'None'

class Artisan:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 6
        self.name = 'Artisan'
        self.type = 'Action'
        self.used = False
        self.subtype = 'None'

    def action(self, Player, game, Plist):
        cardno = int(input("Which card would you like to gain? "))
        try:
            if game.deck_index[cardno][1][0].cost > 5:
                print("The card must be worth less than 6! ")
                self.action(Player, game)
            else:
                Player.hand.append(game.deck_index[cardno][1][0])
                game.deck_index[cardno][1] = game.deck_index[cardno][1][:len(game.deck_index[cardno][1]) - 1]
        except ValueError:
            print("There aren't any left! ")

        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 6
        self.name = 'Artisan'
        self.type = 'Action'
        self.used = True
        self.subtype = 'None'

class Bandit:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Bandit'
        self.type = 'Action'
        self.subtype = 'Attack'
        self.used = False


    def action(self, Player, game, Plist):
        Player.take_card(16, game, Player.discard)
        for x in Plist:
            print("Player ", x.number)
            templist = x.reveal(2)
            print(templist)
            if templist[0].type == 'Treasure' and templist[0].name != 'Copper' and templist[1].type =='Treasure' and templist[1].name !='Copper':
                print("Both can be trashed")
                choice = [int(d) for d in input('Which card would you like to trash, and which would you like to discard? ')]
                print(choice)
                game.trash_list.append(templist[choice[0]])
                x.discard.append(templist[choice[1]])
                pass
            elif (templist[0].type != 'Treasure' or templist[0].name == 'Copper') and (templist[1].type != 'Treasure' or templist[1].name =='Copper'):
                print("Neither is to be trashed")
                x.discard.extend(templist)
            else:
                print("One is a to be trashed, one is not")
                if templist[0].type == 'Treasure' and templist[0].name != 'Copper':
                    game.trash_list.append(templist[0])
                    x.discard.append(templist[1])
                else:
                    game.trash_list.append(templist[1])
                    x.discard.append(templist[0])
                    
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Bandit'
        self.type = 'Action'
        self.subtype = 'Attack'
        self.used = True
        

class Bureaucrat:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Bureaucrat'
        self.type = 'Action'
        self.subtype = 'Attack'
        self.used = False

    def action(self, Player, game, Plist):
        Player.take_card(15, game, Player.deck)
        for x in Plist:
            done = False
            for y in x.hand:
                if y.type == 'Victory' and done == False:
                    x.deck.insert(0, y)
                    x.hand.remove(y)
                    done = True
                else:
                    pass
                    
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Beaureaucrat'
        self.type = 'Action'
        self.subtype = 'Attack'
        self.used = True

class Cellar:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Cellar'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        discarded = 0
        while True:
            templist = []
            for Card in range (len(Player.hand)):
                templist.extend([str(Card) + ' : ' + Player.hand[Card].name])
            print(templist)
            try:
                choice = int(input("Which card would you like to discard? Press enter to stop. "))
                if Player.hand[choice] == self:
                    print("You can't discard a Cellar that is in use. ")
                else:
                    Player.discard_card(choice)
                    discarded += 1
            except ValueError:
                break

        self.pval = 0
        self.pvic = 0
        self.pcar = discarded
        self.pact = 1
        self.pbuy = 0
        self.cost = 2
        self.name = 'Cellar'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Chapel:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Chapel'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        try:
            for x in range(4):
                templist = []
                for Card in range (len(Player.hand)):
                    templist.extend([str(Card) + ' : ' + Player.hand[Card].name])
                print(templist)
                choice = int(input("Which card would you like to trash? Press enter to stop. "))
                game.trash(Player.hand[choice], Player.hand)
        except ValueError:
            pass
        except IndexError:
            print("That card doesn't exist!")
        
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Chapel'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Council_Room:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Council_Room'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        for x in Plist:
            x.draw(1)
        self.pval = 0
        self.pvic = 0
        self.pcar = 4
        self.pact = 0
        self.pbuy = 1
        self.cost = 5
        self.name = 'Council Room'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Festival:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Festival'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        self.pval = 2
        self.pvic = 0
        self.pcar = 0
        self.pact = 2
        self.pbuy = 1
        self.cost = 5
        self.name = 'Festival'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True


class Gardens:
    def __init__ (self):
        self.pval = 0
        self.pvic = 0 #deck/10
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Gardens'
        self.type = 'Victory'
        self.subtype = 'None'

    def game_end(self, Player, deck):
        self.pvic = math.floor(len(deck)/10)

class Harbinger:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 3
        self.name = 'Harbinger'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):  
        Player.draw(1)
        for x in range(len(Player.discard)):
            print(x, Player.discard[x].name)
        choice = int(input("Which card would you like to move to your deck? "))
        Player.deck.insert(0, Player.discard[choice])
        Player.discard.remove(Player.discard[choice])

        self.pval = 0
        self.pvic = 0
        self.pact = 1
        self.pbuy = 0
        self.cost = 3
        self.name = 'Harbinger'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Laboratory:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Laboratory'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        
        self.pval = 0
        self.pvic = 0
        self.pcar = 2
        self.pact = 1
        self.pbuy = 0
        self.cost = 5
        self.name = 'Laboratory'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Library:
    def __init__ (self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Library'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False
    def action(self, Player, game, Plist):
        templist = []
        while len(Player.hand) < 7:
            j = 0
            print(len(Player.hand))
            Player.draw(1)
            print('You drew', Player.hand[-1].name)
            if Player.hand[-1].type == 'Action':
                while j == 0:
                    choice = int(input('What would you like to do with it? 0 for discard, 1 for keep '))
                    if choice == 0:
                        templist.append(Player.hand[-1])
                        Player.hand.remove(Player.hand[-1])
                        j = 1
                    elif choice == 1:
                        j = 1
                    else:
                        pass
        Player.discard.extend(templist)
        templist = []
                
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Library'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Market:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Market'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        
        self.pval = 1
        self.pvic = 0
        self.pcar = 1
        self.pact = 1
        self.pbuy = 1
        self.cost = 5
        self.name = 'Market'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Merchant:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 3
        self.name = 'Merchant'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def silver_check(self, Player, game, Plist):
        Silver_Found = False
        while Player.play == True:
            while Silver_Found == False:
                for x in Player.hand:
                    if isinstance(x, Silver):
                        print("gain +1 value from Merchant")
                        game.value_added += 1
                        Player.prop_check(game)
                        Silver_Found = True
                        break
            break

    def action(self, Player, game, Plist):
        check_thread = threading.Thread(target = self.silver_check, args = (Player, game, Plist))
        check_thread.start()
        self.pval = 0
        self.pvic = 0
        self.pcar = 1
        self.pact = 1
        self.pbuy = 0
        self.cost = 3
        self.name = 'Merchant'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Militia:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 6
        self.name = 'Militia'
        self.type = 'Action'
        self.subtype = 'Attack'
        self.used = False

    def action(self, Player, game, Plist):
        for Other in Plist:
            while len(Other.hand) > 3:
                templist = []
                print('Player', Other.number, '\n')
                for y in range(len(Other.hand)):
                    templist.extend([str(y) + ': ' +Other.hand[y].name])
                print(templist)
                choice = int(input("Which card would you like to discard? "))
                Other.discard_card(choice)

  
        self.pval = 2
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Militia'
        self.type = 'Action'
        self.subtype = 'Attack'
        self.used = True

class Mine:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 6
        self.name = 'Mine'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False
    def action(self, Player, game, Plist):
        templist = []
        for Card in range (len(Player.hand)):
            if Player.hand[Card].type == 'Treasure':
                templist.append( str(Card) + ': ' + Player.hand[Card].name)
        print(templist)
        choice = int(input('Which card would you like to trash? '))
        max_value = Player.hand[choice].cost + 3
        game.trash(Player.hand[choice], Player.hand)

        templist = []
        for cards in range (len(game.deck_index)):
            if len(game.deck_index[cards][1]) > 0:
                if game.deck_index[cards][1][0].cost <= max_value and game.deck_index[cards][1][0].type == 'Treasure':
                    templist.append(str(cards) + ': ' + game.deck_index[cards][1][0].name)
        print(templist)
        choice = int(input('Which card would you like to gain? '))
        Player.take_card(choice, game, Player.hand)
        
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 5
        self.name = 'Mine'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Moat:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Moat'
        self.type = 'Action'
        self.subtype = 'Reaction'
        self.used = False
        self.reaction_used = False

    def reaction_conditions(self, Player, game, Plist):
        return True

    def action(self, Player, game, Plist):
        self.pval = 0
        self.pvic = 0
        self.pcar = 2
        self.pact = 0
        self.pbuy = 0
        self.cost = 2
        self.name = 'Moat'
        self.type = 'Action'
        self.subtype = 'Reaction'
        self.used = True

class Moneylender:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Moneylender'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False

    def action(self, Player, game, Plist):
        for card in Player.hand:
            if card.name == 'Copper':
                game.trash(card, Player.hand)
                self.pval = 3
                break
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Moneylender'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Poacher:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Poacher'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False
    def action(self, Player, game, Plist):
        discard_tot = game.check_end(game, Plist, Player)
        for x in range(discard_tot):
            game.index_list(Player.hand)
            choice = int(input('Which card would you like to discard? '))
            Player.discard_card(choice)
            
        self.pval = 1
        self.pvic = 0
        self.pcar = 1
        self.pact = 1
        self.pbuy = 0
        self.cost = 4
        self.name = 'Poacher'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Remodel:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Remodel'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False
    def action(self, Player, game, Plist):
        templist = []
        game.index_list(Player.hand)
        choice = int(input('Which card would you like to trash? '))
        if Player.hand[choice] == self:
            print('You may not trash the card in use! ')
            self.action(Player, game, Plist)
        else:
            max_value = Player.hand[choice].cost + 2
            game.trash(Player.hand[choice], Player.hand)

            for cards in range (len(game.deck_index)):
                if len(game.deck_index[cards][1]) > 0:
                    if game.deck_index[cards][1][0].cost <= max_value:
                        templist.append(str(cards) + ': ' + game.deck_index[cards][1][0].name)
            print(templist)
            choice = int(input('Which card would you like to gain? '))
            Player.take_card(choice, game, Player.hand)

        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Remodel'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

class Sentry:
    def __init__(self):
        self.pval = 0
        self.pvic = 0
        self.pcar = 0
        self.pact = 0
        self.pbuy = 0
        self.cost = 4
        self.name = 'Sentry'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = False
    def action(self, Player, game, Plist):
        revealed_cards = Player.reveal(2)
        game.index_list(revealed_cards)
        

        self.pval = 0
        self.pvic = 0
        self.pcar = 1
        self.pact = 1
        self.pbuy = 0
        self.cost = 4
        self.name = 'Sentry'
        self.type = 'Action'
        self.subtype = 'None'
        self.used = True

card_list = {
    'Copper' : [Copper, 0],
    'Silver' : [Silver, 3],
    'Gold' : [Gold, 6],
    'Estate' : [Estate, 2],
    'Duchy' : [Duchy, 5],
    'Province' : [Province, 8],
    'Curse' : [Curse, 0],
    'Artisan' : [Artisan, 6],
    'Bandit' : [Bandit, 2],
    'Bureaucrat' : [Bureaucrat, 4],
    'Cellar' : [Cellar, 2],
    'Chapel' :[Chapel, 2],
    'Council_Room' : [Council_Room, 5],
    'Festival' : [Festival, 5],
    'Gardens' : [Gardens, 4],
    'Harbinger' : [Harbinger, 3],
    'Laboratory' : [Laboratory, 5],
    'Library' : [Library, 5],
    'Market' : [Market, 5],
    'Merchant' : [Merchant, 5],
    'Militia' : [Militia, 4],
    'Mine' : [Mine, 5],
    'Moat' : [Moat, 2],
    'Moneylender' : [Moneylender, 4],
    'Poacher' : [Poacher, 4],
    'Remodel' : [Remodel, 4],
    'Sentry' : [Sentry, 5]
}



            
