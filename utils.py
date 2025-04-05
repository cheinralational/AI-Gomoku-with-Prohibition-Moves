import pygame

BOARD_SIZE = 15
GRID_SIZE = 40
MARGIN = 30
PIECE_RADIUS = 18
WINDOW_SIZE = BOARD_SIZE * GRID_SIZE + 2 * MARGIN
BUTTON_HEIGHT = 50  # 按钮高度

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_COLOR = (220, 179, 92)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)

# 初始化按钮
restart_button = pygame.Rect(WINDOW_SIZE // 2 - 100, WINDOW_SIZE + 10, 200, 40)

# 字体
font = pygame.font.SysFont('SimHei', 36)
button_font = pygame.font.SysFont('SimHei', 24)
