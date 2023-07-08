import pygame as pg
from NormalCard import NormalCard
from DrawingPile import DrawingPile

class GUIManager():

    def __init__(self, window_size: tuple, background_color: str, font: pg.font):
        self.window_size = window_size
        self.background_color = background_color
        self.font = font
        self.clickableList: list[list[pg.Rect, NormalCard]] = [] 
        

    def drawTopCard(self, topCard:NormalCard, ) -> pg.Surface:
        TCimg = pg.image.load(topCard.path)
        TCmessage = self.font.render("The Current Card:", True, (0,0,0))
        surfaceTC = pg.Surface((180, 110))
        surfaceTC.fill(self.background_color) 
        surfaceTC.blit(TCmessage, (0, 0))
        surfaceTC.blit(TCimg, (0, 20))
        return surfaceTC
    
    def drawPlayerDeck(self, playerCards: list[NormalCard], surface_start: tuple) -> pg.Surface:
        PCimgs = [pg.image.load(playerCards[i].path) for i in range(0, len(playerCards))]
        PCmessage = self.font.render("Your Cards:", True, (0,0,0))
        surfacePC = pg.Surface((len(playerCards)*50, 105))
        surfacePC.fill(self.background_color)
        surfacePC.blit(PCmessage, (0,0))
        for i in range(0, len(playerCards)):
            surfacePC.blit(PCimgs[i], (50*i, 25))
            self.clickableList.append([pg.Rect((50*i+5)+surface_start[0], 25+surface_start[1], 48, 74), playerCards[i]])
        return surfacePC
    
    def drawDrawingDeck(self, surface_start: tuple, deck: DrawingPile) -> pg.Surface:
        DDimg = pg.image.load(r"C:\Users\mk07\CardGameCollection\Uno\Images\cardBack.png")
        DDmessage = self.font.render("Draw a new Card:", True, (0,0,0))
        surfaceDD = pg.Surface((180, 110))
        surfaceDD.fill(self.background_color)
        surfaceDD.blit(DDmessage, (0,0))
        surfaceDD.blit(DDimg, (0, 20))
        self.clickableList.append([pg.Rect(surface_start[0], surface_start[1]+20, 48,74), deck])
        return surfaceDD
    
    def drawError(self, errorindex: int):
        errors = ["That card is not playable!"]
        errormessage = self.font.render(errors[errorindex], True, (0,0,0))
        return errormessage