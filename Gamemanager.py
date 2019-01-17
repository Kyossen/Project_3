# usr/env/bin Python3.4
# coding:utf-8

# Import file
from Player import *
from Item import *

# Import Lib
import random
import sys

class GameManager:

    # Init the player and the maze
    def __init__(self, maze):
        self.maze = maze
        self.player = Player(self.maze.get_player_position())

        # Find the positions empty for the spawn of items and add this positions in list for spawn
        spaces = self.maze.get_all_positions(" ")
        list_items = ['G', 'H', 'I']
        self.list_item_class = []
        for item in list_items:
            pos = random.choice(spaces)
            spaces.remove(pos)
            self.list_item_class.append(Item(pos, item))
        # Use this list in a loop then use method for spawn
        for spawn_item in self.list_item_class:
            self.maze.spawn_item(spawn_item)

    # Create a loop for playing, print and manage this game
    def start_game(self):
        # This is a rappel for move commands
        print("Commands for playing the maze game:")
        print("Z -> moveUp|S -> moveDown|D -> moveRight|Q -> moveLeft|")
        while self.player != "E":
            # Print the maze and get player position
            print(self.maze)
            new_position = self.player.move_player()

            # Check if player in the maze or out
            if self.maze.true_or_false_pos(new_position) == True:
                new_symbol = self.maze.get_symbol_at_position(new_position)
            else:
                new_symbol = None

            # Check the new symbol for move
            if new_symbol == " ":
                self.maze.writ_symbol(new_position, "@")
            # If new symbol is the item then I pick up this item
            elif new_symbol == "G" or new_symbol == "H" or new_symbol == "I":
                self.maze.writ_symbol(new_position, "@")
                print("I have pick up a item !")
                self.player.add_item(new_symbol)
            # If new symbol is the endgame, the guard check my inventory
            elif new_symbol == "E":
                if len(self.player.stock) == 3:
                    self.maze.writ_symbol(new_position, "@")
                    print("It's done ... Good game :) !")
                else:
                    print("Your is Dead...")
                    sys.exit()
            # If new symbol isn't items, endgame or a empty position, I replace my position to old position
            else:
                self.player.rollback()

            # I writ on my old position a empty position for don't clone player
            if new_symbol != "x" and new_symbol != None:
                old_position = self.player.old_position
                self.maze.writ_symbol(old_position, " ")
