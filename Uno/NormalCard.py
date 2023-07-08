import pygame as pg


class NormalCard():
    def __init__(self, color: str, value: str):
        self.color = color
        self.value = value
        self.path = self.path = rf"C:\Users\mk07\CardGameCollection\Uno\Images\{self.color}{self.value}.png"

    def iscardplayable(self, currentCard) -> bool:
        if currentCard.value == self.value or currentCard.color == self.color or self.color=="w":
            return True
        return False
    
    
    
