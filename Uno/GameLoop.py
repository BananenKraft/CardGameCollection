from DrawingPile import DrawingPile
from DiscardPile import DiscardPile
from GUIManager import GUIManager
from GameManager import GameManager
import os, sys
import random
import pygame as pg

# Init pygame
pg.init()
window_size=(1000,500)
background_color = "grey"
screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()
font = pg.font.SysFont(None, 24)
running = True
errortimer = 0

# Initialize the GUIManager which is responible for drawing the objects
guimanager = GUIManager(window_size, background_color, font)

# Initialize the GameManager which is responisble for handling game logic
gamemanager = GameManager()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for button in guimanager.clickableList:
                    if button[0].collidepoint(pos):
                        if type(button[1]) == DrawingPile:
                            gamemanager.cardDrawn()
                        else:
                            if gamemanager.iscardplayable(button[1]):
                                gamemanager.cardPlayed(button[1])
                            else:
                                errortimer = 300
                                 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)

    # constants
    curr_y = 5
    errortimer -= 1


    # TODO: somehow get absolute position of rects
    guimanager.clickableList = []

    # draw Current Top Card
    screen.blit(guimanager.drawTopCard(gamemanager.discardPile.cards[-1]), (10, curr_y))

    # draw drawing Deck
    screen.blit(guimanager.drawDrawingDeck((190,curr_y), gamemanager.drawingPile), (190, curr_y))

    curr_y += 105
        
    # draw Player Deck
    screen.blit(guimanager.drawPlayerDeck(gamemanager.playerCards, (10, curr_y)), (10,curr_y))
    curr_y += 120

    # draw Errors
    if errortimer > 0:
        screen.blit(guimanager.drawError(0), (10, curr_y))
        curr_y += 20

    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()


