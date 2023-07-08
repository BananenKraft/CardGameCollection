from NormalCard import NormalCard
from Pile import Pile
import random

class DrawingPile(Pile):
    def __init__(self):
        super().__init__()
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
                self.cards.append(NormalCard(c,"s"))
                self.cards.append(NormalCard(c,"r"))
                self.cards.append(NormalCard(c,"d2"))
        for i in range(0,4):
            self.cards.append(NormalCard("w","pc"))
            self.cards.append(NormalCard("w","d4"))
        self.decksize += 108
    
  

