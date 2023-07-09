from DrawingPile import DrawingPile
from DiscardPile import DiscardPile
from NormalCard import NormalCard
from GUIManager import GUIManager
import os, sys
import random
import pygame as pg


class GameManager():
    def __init__(self) -> None:
        # Build the Deck of Cards
        self.drawingPile = DrawingPile()
        self.discardPile = DiscardPile()
        # get starting card in the Middle
        self.GenenrateStartingCard()
        # create Player Deck
        self.playerCards = [self.drawingPile.removeTopCard() for i in range(0,7)]
    
    def GenenrateStartingCard(self):
        illegalstartingValues = ["pc","d4","d2","s","r"]
        while True:
            topCard = self.drawingPile.removeTopCard()
            if topCard.value in illegalstartingValues:
                self.drawingPile.addCard(topCard)
            else: 
                break
        self.discardPile.addCard(topCard)

    def iscardplayable(self, currentCard: NormalCard) -> bool:
        compareCard = self.discardPile.cards[-1]
        if currentCard.value == compareCard.value or currentCard.color == compareCard.color or compareCard.color=="w" or currentCard.color == "w":
            return True
        return False

    def cardDrawn(self): 
        self.playerCards.append(self.drawingPile.removeTopCard())

    def cardPlayed(self, cardPlayed: NormalCard,) -> bool:
        self.playerCards.remove(cardPlayed)
        self.discardPile.cards.append(cardPlayed)
        print(cardPlayed.value)
        match cardPlayed.value:
            # Normal Cards, nothin happends
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                pass
            # TODO: Make a color picking GUI appear
            case "pc" | "d4":
                GUIManager.drawPickColor()
            

