from NormalCard import NormalCard
from SpecialCard import SpecialCard
from UnoCard import UnoCard
import random

class Deck():
    def __init__(self):
        self.cards = []
        self.decksize = 108
        self.buildDeck()
        self.shuffleDeck()
        
            
    def buildDeck(self):
        # Build Card deck
        suits = ["r","b","g","y"]
        for c in suits:
            for i in range(0,10):
                self.cards.append(NormalCard(c,str(i)))
            for i in range(1,10):
                self.cards.append(NormalCard(c,str(i)))
            for i in range(0,2):
                self.cards.append(SpecialCard(c,"s"))
                self.cards.append(SpecialCard(c,"r"))
                self.cards.append(SpecialCard(c,"d2"))
        for i in range(0,4):
            self.cards.append(SpecialCard("w","pc"))
            self.cards.append(SpecialCard("w","d4"))

    def shuffleDeck(self):
        for i in range(0,1000000):
            self.switchTwoCards(random.randint(0,self.decksize-1), random.randint(0,self.decksize-1))

    def switchTwoCards(self, cardindex1, cardindex2):
        placeholder = self.cards[cardindex1]
        self.cards[cardindex1] = self.cards[cardindex2]
        self.cards[cardindex2] = placeholder
    
    def removeTopCard(self) -> UnoCard:
        self.decksize -= 1
        return self.cards.pop(self.decksize)
        
