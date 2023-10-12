import pygame as pg

class Clickable:
    def __init__(self, rect: pg.Rect, identifier: str, reference = None) -> None:
        self.rect = rect
        self.identifier = identifier
        self.reference = reference
