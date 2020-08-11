import random
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
suits=('Hearts','Diamond','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack',
'Queen','King','Ace')
class Card:
    def __init__(self,suit,ranks):
        self.suit=suit
        self.ranks=ranks
        self.value=values[ranks]

    def __str__(self):
        return self.rank+" of "+self.suit

class Deck:
    def __init__(self):
        self.allCards=[]

        for suit in suits:
            for rank in ranks:
                createdCard=Card(suit,rank)
                self.allCards.append(createdCard)

    def shuffle(self):
        random.shuffle(self.allCards)

    def dealOne(self):
        return self.allCards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.allCards=[]

    def removeOne(self):
        return self.allCards.pop(0)

    def addCards(self,newCards):
        if type(newCards)==type([]):
            #list of multiple card objects 
            self.allCards.extend(newCards)
        else:
            #for a single card objects
            self.allCards.append(newCards)
        
    def __str__(self):
        return f'Player {self.name} has {len(self.allCards)} cards.'

#Game setup
playerOne=Player('One')
playerTwo=Player('Two')

newDeck=Deck()
newDeck.shuffle()

for x in range(26):
    playerOne.addCards(newDeck.dealOne())
    playerTwo.addCards(newDeck.dealOne())

gameOn=True
roundNum=0

while gameOn:
    roundNum+=1
    print(f"Round {roundNum}")

    if len(playerOne.allCards)==0:
        print("Player One, out of cards! \nPlayer Two wins!")
        gameOn=False
        break
    if len(playerTwo.allCards)==0:
        print("Player Two , out of cards! \nPlayer One wins!")
        gameOn=False
        break
    
    #Start a new round
    playerOneCards=[]
    playerOneCards.append(playerOne.removeOne())

    playerTwoCards=[]
    playerTwoCards.append(playerTwo.removeOne())

    #At War
    atWar=True

    while atWar:
        if playerOneCards[-1].value>playerTwoCards[-1].value:
            playerOne.addCards(playerOneCards)
            playerOne.addCards(playerTwoCards)
            atWar=False
        
        elif playerOneCards[-1].value<playerTwoCards[-1].value:
            playerTwo.addCards(playerOneCards)
            playerTwo.addCards(playerTwoCards)
            atWar=False
        
        else:
            print("WAR!")
            if len(playerOne.allCards)<15:
                print("Player One unable to declare war \nPlayer Two wins!")
                gameOn=False
                break
            
            elif len(playerTwo.allCards)<15:
                    print("Player Two unable to declare war \nPlayer One wins!")
                    gameOn=False
                    break
                
            else:
                for num in range(15):
                    playerOneCards.append(playerOne.removeOne())
                    playerTwoCards.append(playerTwo.removeOne())

