import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30
GRID_X_OFFSET = 50
GRID_Y_OFFSET = 50
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + 2 * GRID_X_OFFSET + 200
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 2 * GRID_Y_OFFSET

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)

# Funny piece shapes (some are intentionally weird)
PIECES = {
    'I': [['.....',
           '..#..',
           '..#..',
           '..#..',
           '..#..'],
          ['.....',
           '.....',
           '####.',
           '.....',
           '.....']],
    
    'O': [['.....',
           '.....',
           '.##..',
           '.##..',
           '.....']],
    
    'T': [['.....',
           '.....',
           '.#...',
           '###..',
           '.....'],
          ['.....',
           '.....',
           '.#...',
           '.##..',
           '.#...'],
          ['.....',
           '.....',
           '.....',
           '###..',
           '.#...'],
          ['.....',
           '.....',
           '.#...',
           '##...',
           '.#...']],
    
    'S': [['.....',
           '.....',
           '.##..',
           '##...',
           '.....'],
          ['.....',
           '.#...',
           '.##..',
           '..#..',
           '.....']],
    
    'Z': [['.....',
           '.....',
           '##...',
           '.##..',
           '.....'],
          ['.....',
           '..#..',
           '.##..',
           '.#...',
           '.....']],
    
    'J': [['.....',
           '.#...',
           '.#...',
           '##...',
           '.....'],
          ['.....',
           '.....',
           '#....',
           '###..',
           '.....'],
          ['.....',
           '.##..',
           '.#...',
           '.#...',
           '.....'],
          ['.....',
           '.....',
           '###..',
           '..#..',
           '.....']],
    
    'L': [['.....',
           '..#..',
           '..#..',
           '.##..',
           '.....'],
          ['.....',
           '.....',
           '###..',
           '#....',
           '.....'],
          ['.....',
           '##...',
           '.#...',
           '.#...',
           '.....'],
          ['.....',
           '.....',
           '..#..',
           '###..',
           '.....']]
}

PIECE_COLORS = {
    'I': CYAN,
    'O': YELLOW,
    'T': PURPLE,
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': ORANGE
}

# Funny messages
FUNNY_MESSAGES = [
    "Oops! Gravity wins again!",
    "That piece had commitment issues!",
    "Physics: 1, You: 0",
    "The blocks are rebelling!",
    "Tetris pieces don't like being told what to do!",
    "That's not how geometry works!",
    "The blocks are having an existential crisis!",
    "Gravity is not your friend today!",
    "The pieces are practicing social distancing!",
    "That block just wanted to be free!"
]

LINE_CLEAR_MESSAGES = [
    "BOOM! Lines go bye-bye!",
    "Satisfying block destruction!",
    "The blocks have been vanquished!",
    "Poof! Magic line disappearing act!",
    "The great block purge of today!",
    "Lines cleared with extreme prejudice!",
    "Block genocide in progress!",
    "The blocks didn't see it coming!",
    "Surprise! Your lines are gone!",
    "The blocks have left the building!"
]

class FunnyTetris:
    def __init__(self):
        self.screen = pygame