# usr/env/bin Python3.4
# coding:utf-8

# Import file
from Gamemanager import GameManager
from Maze import Maze
from Gui import Game_GUI

# Import Lib
import argparse

# Create a pars for user choice
def parser_game():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--Terminal",  action='store_true' ,help="Game in The terminal")
    parser.add_argument("-g", "--GUI", action='store_true' ,help="Game in The GUI")
    args = parser.parse_args()
    return args

# Create a main for run this applications
if __name__ == "__main__":
    maze = Maze("maze_1.txt")
    args = parser_game()
    gamemanager = GameManager(maze)
    if args.Terminal:
        gamemanager.start_game()
    else:
        gui = Game_GUI(maze, gamemanager.list_item_class)
        gui.on_loop_game()

    
    
            #Tableaux adouble dimensions (liste les unes dans les autres)
        #Corriger fautes
        #Définir les classes dans la partie algorithme les classes
        #Basé l'algo sur chaque classe gràace aux positions
        #Diapo pour la soutenance
        #Nom du projet avec nom et parcours
        #Trois points (labyrinth, fichier editable)
        #Trois icones pycharm, pygame, python
        #PowerPoint
        #Keynote
