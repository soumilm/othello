import sys
import pygame
import time
import tiles
import board
pygame.init()

bd = board.Board(tiles.STARTING_TILES)

_, _, width, height = bd.get_rect_val()
size = width, height

black = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    bd.draw_board(screen)
    pygame.display.flip()
    time.sleep(0.05)