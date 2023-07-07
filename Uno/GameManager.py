from Deck import Deck
from GUIManager import GUIManager
import os, sys
import random
import pygame as pg

# Init pygame
pg.init()
window_size=(800,500)
background_color = "grey"
screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()
font = pg.font.SysFont(None, 24)
running = True

# Initialize the GUIManager which is responible for drawing the objects
guimanager = GUIManager(window_size, background_color, font)

# Build the Deck of Cards
deck = Deck()

# get starting card in the Middle
topCard = deck.getStartingCard()

# create Player Deck
playerCards = [deck.removeTopCard() for i in range(0,7)]


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)

    # const for keeping track of vertical space available
    curr_y = 5

    # draw Current Top Card
    screen.blit(guimanager.drawTopCard(topCard), (10, curr_y))
    curr_y += 110
        

    # draw Player Deck
    screen.blit(guimanager.drawPlayerDeck(playerCards), (10,curr_y))
    curr_y += 105

    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()


