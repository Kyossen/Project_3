# usr/env/bin Python3.4
# coding:utf-8

# Import Lib
import platform

# Import module
from pygame.locals import *
import pygame

# Import file
from Player import Player
from Maze import Maze
from Item import Item

class WallSprite(pygame.sprite.Sprite):
    """Create a class for manage the character sprites"""
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

class CharactereSprite(pygame.sprite.Sprite):
    """Create a class for manage the player sprite"""
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def move(self, new_pos):
        player_pos = 40
        self.rect.x = new_pos[0] * player_pos
        self.rect.y = new_pos[1] * player_pos

class Game_GUI:

    def __init__(self, maze, items):
        """Init the game"""
        pygame.init()
        self.windowWidth = 600
        self.windowHeight = 480
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE)
        pygame.display.set_caption('The Maze')
        self.maze = maze
        self.player = Player(self.maze.get_player_position())
        self.items = items
        self.clock = pygame.time.Clock()
        self.running = True

        # Init of the variable for the condition of endgame
        self.a = True

        # Init the pics for sprites and define user os of user
        if platform.system() == "Windows":
            self.img_player = pygame.image.load("ressource\MacGyver.png")
            self.img_background = pygame.image.load("ressource\Background.png")
            self.img_walls = pygame.image.load("ressource\Wall.png")
            self.img_npc = pygame.image.load("ressource\Gardien.png")
            self.img_item_1 = pygame.image.load(r"ressource\baton.png")
            self.img_item_2 = pygame.image.load("ressource\pipe.png")
            self.img_item_3 = pygame.image.load("ressource\potion.png")
            self.img_end_game = pygame.image.load("ressource\youdied.png")
            self.img_win_game = pygame.image.load("ressource\youwin.png")
        else:
            self.img_player = pygame.image.load("ressource/MacGyver.png")
            self.img_background = pygame.image.load("ressource/Background.png")
            self.img_walls = pygame.image.load("ressource/Wall.png")
            self.img_npc = pygame.image.load("ressource/Gardien.png")
            self.img_item_1 = pygame.image.load(r"ressource/baton.png")
            self.img_item_2 = pygame.image.load("ressource/pipe.png")
            self.img_item_3 = pygame.image.load("ressource/potion.png")
            self.img_end_game = pygame.image.load("ressource/youdied.png")
            self.img_win_game = pygame.image.load("ressource/youwin.png")

        # Init the sprites
        self.sprite_player = CharactereSprite(self.img_player)
        self.sprite_items = [WallSprite(self.img_item_1), WallSprite(self.img_item_2), WallSprite(self.img_item_3)]
        self.items_list_sprite = pygame.sprite.Group()
        self.character_sprites_list = pygame.sprite.Group()
        self.wall_sprites_list = pygame.sprite.Group()
        self.character_sprites_list.add([self.sprite_player])
        self.items_list_sprite.add(self.sprite_items)

    def draw_and_move_player(self):
        """Get the position for the player and move player"""
        pos = self.player.x, self.player.y
        self.sprite_player.move(pos)

    def draw_npc(self):
        """Draw Guard"""
        self.npc = self.maze.get_all_positions("E")
        for draw in self.npc:
            npc_sprite = CharactereSprite(self.img_npc)
            npc_sprite.rect.x = draw[0] * 40
            npc_sprite.rect.y = draw[1] * 40
            self.character_sprites_list.add(npc_sprite)

    def draw_wall(self):
        """Draw walls"""
        self.walls = self.maze.get_all_positions("x")
        for draw in self.walls:
            wall_sprite = WallSprite(self.img_walls)
            wall_sprite.rect.x = draw[0] * 40
            wall_sprite.rect.y = draw[1] * 40
            self.wall_sprites_list.add(wall_sprite)

    def draw_inventory(self):
        """Draw rect for inventory on side right"""
        white = (255, 255, 255)
        black = (0, 0, 0)
        pygame.draw.rect(self.screen, white, (565, 200, 40, 40), 0)
        pygame.draw.rect(self.screen, white, (565, 240, 40, 40), 0)
        pygame.draw.rect(self.screen, white, (565, 280, 40, 40), 0)
        pygame.draw.rect(self.screen, black, (565, 200, 40, 40), 5)
        pygame.draw.rect(self.screen, black, (565, 240, 40, 40), 5)
        pygame.draw.rect(self.screen, black, (565, 280, 40, 40), 5)

    def draw_items(self):
        """Draw Items on the map"""
        items = self.items
        for index, item in enumerate(items):
            self.sprite_items[index].rect.x = item.x * 40
            self.sprite_items[index].rect.y = item.y * 40

    def rollback(self):
        """Replace player position to old player position"""
        self.player.x = self.old_position[0]
        self.player.y = self.old_position[1]

    def draw_base(self):
        """Print a party the game"""
        self.screen.blit(self.img_background, (0, 0))
        self.wall_sprites_list.draw(self.screen)
        self.draw_inventory()
        self.items_list_sprite.update()
        self.items_list_sprite.draw(self.screen)
        self.draw_and_move_player()
        self.draw_npc()
        self.character_sprites_list.update()
        self.character_sprites_list.draw(self.screen)

    def on_loop_game(self):
        """Create a loop for playing, print and manage this game"""
        self.draw_base()
        self.draw_wall()
        self.draw_items()
        while self.running:
            # For close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return
                # Get last position for the player
                self.old_position = self.player.x, self.player.y

                # Move the player
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.player.moveUp()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.player.moveDown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.player.moveLeft()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.player.moveRight()
                break
            self.new_position = self.player.x, self.player.y
            if self.new_position != self.old_position:

                # Check len x and len y for the maze
                if self.maze.true_or_false_pos(self.new_position) == True:
                    self.new_symbol = self.maze.get_symbol_at_position(self.new_position)
                else:
                    self.new_symbol = None
                    self.rollback()

                # Check the new symbol for walls, if wall is true the player move back position
                if self.new_symbol == "x":
                    self.rollback()

                # Check the new symbol for get items
                if self.new_symbol == "G" or self.new_symbol == "H" or self.new_symbol == "I":
                    # Pick up the item and put it in inventory and move the sprite to the right position
                    for idx, item in enumerate(self.items):
                        if self.new_position[0] == item.x and self.new_position[1] == item.y and  item.pickup != True:
                            # The right position is calcul for each round of loop
                            self.sprite_items[idx].rect.x = 565
                            self.sprite_items[idx].rect.y = 200 + 40 * len(self.player.stock)
                            self.items[idx].pickup = True
                            self.player.add_item(self.new_symbol)

                # Check the new symbol for the end of the game
                if self.new_symbol == "E":
                    self.a = False
                    if len(self.player.stock) == 3:
                        self.screen.blit(self.img_win_game, (0, 0))
                    else:
                        self.screen.blit(self.img_end_game, (0, 0))

            # This condition below is used for of the endgame
            # If self.a = True, so we refresh the screen
            # If self.a = False we keep the pics of the endgame

            if self.a == True:
                self.draw_base()
                self.draw_and_move_player()
            # Refresh the screen and manage the images per second
            pygame.display.flip()
            self.clock.tick(60)

#Close the game
pygame.quit()
