# usr/env/bin Python3.4
# coding:utf-8

# Import file
from Player import Player

class Item:
    def __init__(self, position, symbol):
        """Init a class for use items with a position and a symbol. self.pickup = False is use for graphic interface"""
        self.x = position[0]
        self.y = position[1]
        self.symbol = symbol
        self.pickup = False
