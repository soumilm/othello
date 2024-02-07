import copy
from typing import Optional

EMPTY = 0
BLACK = 1
WHITE = 2

NUM_TILES_PER_SIDE = 8

if NUM_TILES_PER_SIDE % 2 != 0:
            raise ValueError("number of tiles per side must be even")

class Tiles:
    def __init__(self, tiles: Optional[list[list[int]]] = None) -> None:
        if tiles is None:
            self.tiles = [[EMPTY] * NUM_TILES_PER_SIDE for _ in range(NUM_TILES_PER_SIDE)]
        else:
            self.tiles = tiles
    
    def __copy__(self):
        return Tiles(copy.deepcopy(self.tiles))
    
    def __getitem__(self, i):
        if not isinstance(i, tuple):
            return self.tiles[i]

        x, y = i
        return self.tiles[x][y]
    
    def __setitem__(self, i, val):
        x, y = i
        self.tiles[x][y] = val
        

STARTING_TILES = Tiles()
        
lrg = NUM_TILES_PER_SIDE // 2
STARTING_TILES[lrg, lrg] = WHITE
STARTING_TILES[lrg-1, lrg-1] = WHITE
STARTING_TILES[lrg-1, lrg] = BLACK
STARTING_TILES[lrg, lrg-1] = BLACK
