import sys
import tiles
import pygame
pygame.init()

green = 0, 127, 0
board_rect = (30, 30, 340, 340)

line_width = 5
line_color = 0, 191, 0

tile_width = 60
half_tile_width = tile_width // 2
spacing = tile_width + line_width
piece_radius = 25




board_width = (line_width + tile_width) * tiles.NUM_TILES_PER_SIDE - line_width
board_height = board_width

board_rect = 0, 0, board_width, board_height

EMPTY = 0
BLACK = 1
WHITE = 2

color_map = { WHITE: (255, 255, 255), BLACK: (0, 0, 0) }


class Board:

    def __init__(self, tiles: tiles.Tiles):
        self.tiles = tiles


    def get_rect_val(self):
        return board_rect

    def draw_board(self, surface):
        pygame.draw.rect(surface, green, board_rect)

        for i in range(tiles.NUM_TILES_PER_SIDE-1):
            pygame.draw.rect(surface, line_color, (tile_width + (tile_width + line_width) * i, 0, line_width, board_height))
            pygame.draw.rect(surface, line_color, (0, tile_width + (tile_width + line_width) * i, board_width, line_width))
        
        for i in range(tiles.NUM_TILES_PER_SIDE):
            for j in range(tiles.NUM_TILES_PER_SIDE):
                val = self.tiles[i][j]
                if val == EMPTY:
                    continue

                ctr = (half_tile_width + i * spacing, half_tile_width + j * spacing)
                pygame.draw.circle(surface, color_map[val], ctr, piece_radius)
            
                
    
