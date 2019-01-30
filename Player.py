#!/usr/bin/env python3
# -*- coding: utf-8 -*-

move_player_True = True

class Player:

    def __init__(self, position):
        """Init the player with inventory and positions"""
        self.x = position[0]
        self.y = position[1]
        self.stock = []

    # Create of the variables for move player
    player = 0
    speed = 1

    def moveRight(self):
        """Create of the methods for move player"""
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def move_player(self):
        """Create of the loop for move the player"""
        while move_player_True:

            # The variable below is use for get the old position of the player
            self.old_position = self.x, self.y
            
            user = input("")
            # Keys for move player in terminal
            if user == "d":
                self.moveRight()
                print("Commands: Z -> moveUp|S -> moveDown|D -> moveRight|Q -> moveLeft|")
                return self.x, self.y
            if user == "z":
                self.moveUp()
                print("Commands: Z -> moveUp|S -> moveDown|D -> moveRight|Q -> moveLeft|")
                return self.x, self.y
            if user == "q":
                self.moveLeft()
                print("Commands: Z -> moveUp|S -> moveDown|D -> moveRight|Q -> moveLeft|")
                return self.x, self.y
            if user == "s":
                self.moveDown()
                print("Commands: Z -> moveUp|S -> moveDown|D -> moveRight|Q -> moveLeft|")
                return self.x, self.y

    def rollback(self):
        """Replace player position to old player position"""
        self.x = self.old_position[0]
        self.y = self.old_position[1]

    def add_item(self, stock):
        """Create of the method for add items in inventory"""
        self.stock.append(stock)
