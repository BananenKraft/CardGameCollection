from DrawingPile import DrawingPile
from DiscardPile import DiscardPile
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


    def cardDrawn(self): 
        self.playerCards.append(self.drawingPile.removeTopCard())

    def cardPlayed(self):
        pass