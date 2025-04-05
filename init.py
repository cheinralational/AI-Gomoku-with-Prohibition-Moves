import pygame
import numpy as np
from pygame.locals import *

# 游戏常量（确保这些常量在文件顶部定义）
BOARD_SIZE = 15
GRID_SIZE = 40
MARGIN = 30
PIECE_RADIUS = 18
WINDOW_SIZE = BOARD_SIZE * GRID_SIZE + 2 * MARGIN
BUTTON_HEIGHT = 50

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_COLOR = (220, 179, 92)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)


def init_game():
    """初始化游戏状态"""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + BUTTON_HEIGHT))
    pygame.display.set_caption('摆烂仙君的棋局')
    font = pygame.font.SysFont('SimHei', 36)
    button_font = pygame.font.SysFont('SimHei', 24)

    game_state = {
        'board': np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int),
        'current_player': 1,  # 1: 黑棋(电脑), 2: 白棋(玩家)
        'game_over': False,
        'last_move': None,
        'winner': None,
        'screen': screen,
        'font': font,
        'button_font': button_font,
        'restart_button': pygame.Rect(WINDOW_SIZE // 2 - 100, WINDOW_SIZE + 10, 200, 40)
    }
    return game_state