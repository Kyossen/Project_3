# usr/env/bin Python3.4
# coding:utf-8

# Import Lib
import argparse

# Import file
from Gamemanager import GameManager
from Maze import Maze
from Gui import Game_GUI

def parser_game():
    """Create a pars for user choice"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--Terminal",  action='store_true' ,help="Game in The terminal")
    parser.add_argument("-g", "--GUI", action='store_true' ,help="Game in The GUI")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    """Create a main for run this applications"""
    maze = Maze("maze_1.txt")
    args = parser_game()
    gamemanager = GameManager(maze)
    if args.Terminal:
        gamemanager.start_game()
    else:
        gui = Game_GUI(maze, gamemanager.list_item_class)
        gui.on_loop_game()
