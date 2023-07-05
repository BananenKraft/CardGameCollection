from Deck import Deck
import PySimpleGUI as sg 
import os, sys

deck = Deck()

while True:
    topCard = deck.removeTopCard()
    if topCard.color == "w":
        deck.addcard(topCard)
    else: break

layout =[
    [sg.Text("Current Card:", )],
    [sg.Image(topCard.path)],

# how to display a card  [sg.Image(r"C:\Users\mk07\CardGameCollection\Uno\Images\r0.png")]
]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event,value = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    sg.Image()

window.close()
