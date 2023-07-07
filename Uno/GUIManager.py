import pygame as pg
from NormalCard import NormalCard

class GUIManager():

    def __init__(self, window_size: tuple, background_color: str, font: pg.font):
        self.window_size = window_size
        self.background_color = background_color
        self.font = font

    def drawTopCard(self, topCard:NormalCard):
        TCimg = pg.image.load(topCard.path)
        TCmessage = self.font.render("The Current Card:", True, (0,0,0))
        surfaceTC = pg.Surface((self.window_size[0], 110))
        surfaceTC.fill(self.background_color)
        surfaceTC.blit(TCmessage, (0, 0))
        surfaceTC.blit(TCimg, (0, 20))
        return surfaceTC
    
    def drawPlayerDeck(self, playerCards):
        PCimgs = [pg.image.load(playerCards[i].path) for i in range(0, len(playerCards))]
        PCmessage = self.font.render("Your Cards:", True, (0,0,0))
        surfacePC = pg.Surface((len(playerCards)*50, 105))
        surfacePC.fill(self.background_color)
        surfacePC.blit(PCmessage, (0,0))
        for i in range(0, len(playerCards)):
            surfacePC.blit(PCimgs[i], (50*i, 25))
        return surfacePC
        