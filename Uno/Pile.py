import random
from NormalCard import NormalCard

class Pile():
    def __init__(self):
        self.cards = []
        self.decksize = 0
    
    def removeTopCard(self) -> NormalCard:
        self.decksize -= 1
        return self.cards.pop(self.decksize)
    
    def addCard(self, card):
        self.cards.append(card)
        self.switchTwoCards(random.randint(0,self.decksize), self.decksize)
        self.decksize += 1

    def shuffleDeck(self):
        for i in range(0,1000000):
            self.switchTwoCards(random.randint(0,self.decksize-1), random.randint(0,self.decksize-1))


    def switchTwoCards(self, cardindex1, cardindex2):
        placeholder = self.cards[cardindex1]
        self.cards[cardindex1] = self.cards[cardindex2]
        self.cards[cardindex2] = placeholder