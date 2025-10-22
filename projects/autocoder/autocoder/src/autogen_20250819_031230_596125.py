import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_WIDTH, GRID_HEIGHT = 10, 20
CELL_SIZE = 30
GRID_X = (WIDTH - GRID_WIDTH * CELL_SIZE) // 2
GRID_Y = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)

FUNNY_COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN, PINK]

SHAPES = [
    [['.....',
      '..#..',
      '.###.',
      '.....',
      '.....']],
    [['.....',
      '.....',
      '.##..',
      '.##..',
      '.....']],
    [['.....',
      '.....',
      '.#...',
      '.###.',
      '.....']],
    [['.....',
      '.....',
      '...#.',
      '.###.',
      '.....']],
    [['.....',
      '.....',
      '.##..',
      '..##.',
      '.....']],
    [['.....',
      '.....',
      '..##.',
      '.##..',
      '.....']],
    [['.....',
      '.....',
      '..#..',
      '..#..',
      '..#..']],
]

FUNNY_MESSAGES = [
    "OOPS! Block got dizzy!",
    "WHEEE! Spinning time!",
    "Block says: I'm fabulous!",
    "Gravity? What's that?",
    "BOING BOING BOING!",
    "Block is having an identity crisis!",
    "WIGGLE WIGGLE!",
    "Block learned to dance!",
    "Surprise! I'm a different color now!",
    "Block: Hold my pixels!"
]

class FunnyTetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Funny Tetris - Blocks Gone Wild!")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.fall_time = 0
        self.fall_speed = 500
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.message_font = pygame.font.Font(None, 24)
        self.funny_message = ""
        self.message_timer = 0
        self.shake_offset = [0, 0]
        self.rainbow_mode = False
        self.rainbow_timer = 0
        
    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(FUNNY_COLORS)
        return {
            'shape': shape[0],
            'color': color,
            'x': GRID_WIDTH // 2 - 2,
            'y': 0,
            'rotation': 0,
            'wobble': 0,
            'size_multiplier': 1.0,
            'drunk': False,
            'rainbow': False
        }
    
    def rotate_piece(self, piece):
        rotated = []
        for i in range(len(piece['shape'][0])):
            new_row = ""
            for j in range(len(piece['shape']) - 1, -1, -1):
                new_row += piece['shape'][j][i]
            rotated.append(new_row)
        return rotated
    
    def valid_move(self, piece, dx, dy, shape=None):
        if shape is None:
            shape = piece['shape']
        
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    x, y = piece['x'] + j + dx, piece['y'] + i + dy
                    if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT:
                        return False
                    if y >= 0 and self.grid[y][x]:
                        return False
        return True
    
    def place_piece(self, piece):
        for i, row in enumerate(piece['shape']):
            for j, cell