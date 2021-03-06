# usr/env/bin Python3.4
# coding:utf-8

# Import file
from Gamemanager import GameManager
from Player import Player
from Item import Item

#Import Lib
import sys

# Create class for Maze
class Maze():

    # Init
    def __init__(self, filename):
        with open(filename) as f:
            file = f.read()

            # Transform maze file to list
            self.maze = [list(row) for row in file.splitlines()]

            # Check coordinate
            for line_x in self.maze:
                line_len = len(line_x)
                if line_len != 15:
                    print("You not have the good number to columns.")
                    sys.exit()
            y = len(self.maze)
            if y != 12:
                print("You not have the good number to lines.")

            # Check letter in The maze
            My_spawn_list = []
            x = 0
            y = 0
            for line_s in self.maze:
                if "S" in line_s:
                    My_spawn_list.append("S")
                    x = x + 1
                if "E" in line_s:
                    My_spawn_list.append("E")
                    x = x + 1
            y = y + 1
            x = 0
            if len(My_spawn_list) == 2:
                pass
            else:
                print("You have change or delete a startup letter ...")
                sys.exit()

    def __repr__(self):
        return "\n".join("".join(row) for row in self.maze)

    # Return the startup position for the player
    def get_player_position(self):
        x = 0
        y = 0
        for line in self.maze:
            for c in line:
                if c == "S":
                    return x, y
                x = x + 1
            y = y+1
            x = 0

    # Return all positions for print the  symbol (wall, items, etc...)
    def get_all_positions(self, symbol):
        positions = []
        x = 0
        y = 0
        for line in self.maze:
            for c in line:
                if c == symbol:
                    positions.append((x, y))
                x = x + 1
            y = y+1
            x = 0
        return positions

    """
    Check len x and len y in the maze.
    This method below is use for check that the gamer is in the maze and isn't out.
    """
    def true_or_false_pos(self, position):
        max_x = len(self.maze)
        max_y = len(self.maze[0])
        if position[1] >= max_x:
            return False
        if position[0] >= max_y:
            return False
        else:
            return True

    # Return the symbol of the position the player
    def get_symbol_at_position(self, position):
        get_symbol = self.maze[position[1]][position[0]]
        return get_symbol

    # Write a symbol at position the player
    def writ_symbol(self, position, symbol):
        self.maze[position[1]][position[0]] = symbol

    #Write a symbol on a random position who is selects with the method get_spaces.
    def spawn_item(self, item):
        self.maze[item.y][item.x] = item.symbol
