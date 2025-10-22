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
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE + 2 * GRID_X_OFFSET + 200
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + 2 * GRID_Y_OFFSET

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

# Funny Tetris pieces with silly names
PIECES = {
    'The Awkward Stick': [
        ['....', 'XXXX', '....', '....']
    ],
    'The Clumsy Square': [
        ['XX', 'XX']
    ],
    'The Confused L': [
        ['X..', 'XXX', '...'],
        ['.XX', '.X.', '.X.'],
        ['...', 'XXX', '..X'],
        ['.X.', '.X.', 'XX.']
    ],
    'The Backwards L (Rebel)': [
        ['..X', 'XXX', '...'],
        ['.X.', '.X.', '.XX'],
        ['...', 'XXX', 'X..'],
        ['XX.', '.X.', '.X.']
    ],
    'The Zigzag (Drunk)': [
        ['.XX', 'XX.', '...'],
        ['X..', 'XX.', '.X.']
    ],
    'The Zagzig (Also Drunk)': [
        ['XX.', '.XX', '...'],
        ['.X.', 'XX.', 'X..']
    ],
    'The T-Pose (Asserting Dominance)': [
        ['.X.', 'XXX', '...'],
        ['.X.', '.XX', '.X.'],
        ['...', 'XXX', '.X.'],
        ['.X.', 'XX.', '.X.']
    ]
}

PIECE_COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]

# Funny messages
FUNNY_MESSAGES = [
    "Oops! Gravity wins again!",
    "That piece had commitment issues!",
    "Physics: 1, You: 0",
    "The blocks are rebelling!",
    "Tetris pieces have trust issues!",
    "Gravity is not your friend today!",
    "The blocks are socially distancing!",
    "That was... interesting!",
    "The pieces are having an identity crisis!",
    "Chaos level: Maximum!"
]

class FunnyTetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Funny Tetris - Where Blocks Have Personality!")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.big_font = pygame.font.Font(None, 36)
        
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_time = 0
        self.fall_speed = 500  # milliseconds
        
        self.current_piece = None
        self.current_piece_pos = [0, 0]
        self.current_piece_rotation = 0
        self.current_piece_name = ""
        self.current_piece_color = WHITE
        
        self.message = "Welcome to Funny Tetris!"
        self.message_timer = 0
        
        self.spawn_piece()
    
    def spawn_piece(self):
        piece_names = list(PIECES.keys())
        self.current_piece_name = random.choice(piece_names)
        self.current_piece = PIECES[self.current_piece_name]
        self.current_piece_rotation = 0
        self.current_piece_color = random.choice(PIECE_COLORS)
        self.current_piece_pos = [GRID_WIDTH // 2 - 2