import pygame
from init import *

def draw_board(game_state):
    """绘制棋盘、棋子和按钮"""
    screen = game_state['screen']
    board = game_state['board']
    last_move = game_state['last_move']
    font = game_state['font']
    button_font = game_state['button_font']
    restart_button = game_state['restart_button']

    # 绘制棋盘背景
    screen.fill(BOARD_COLOR, (0, 0, WINDOW_SIZE, WINDOW_SIZE))

    # 绘制网格线
    for i in range(BOARD_SIZE):
        pygame.draw.line(screen, BLACK,
                        (MARGIN, MARGIN + i * GRID_SIZE),
                        (WINDOW_SIZE - MARGIN, MARGIN + i * GRID_SIZE), 1)
        pygame.draw.line(screen, BLACK,
                        (MARGIN + i * GRID_SIZE, MARGIN),
                        (MARGIN + i * GRID_SIZE, WINDOW_SIZE - MARGIN), 1)

    # 绘制天元和星位
    star_points = [3, 7, 11]
    for x in star_points:
        for y in star_points:
            pygame.draw.circle(screen, BLACK,
                              (MARGIN + x * GRID_SIZE, MARGIN + y * GRID_SIZE), 5)

    # 绘制棋子
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == 1:  # 黑棋
                pygame.draw.circle(screen, BLACK,
                                 (MARGIN + x * GRID_SIZE, MARGIN + y * GRID_SIZE), PIECE_RADIUS)
            elif board[y][x] == 2:  # 白棋
                pygame.draw.circle(screen, WHITE,
                                 (MARGIN + x * GRID_SIZE, MARGIN + y * GRID_SIZE), PIECE_RADIUS)

    # 标记最后一步
    if last_move:
        x, y = last_move
        color = RED if board[y][x] == 1 else GREEN
        pygame.draw.circle(screen, color,
                          (MARGIN + x * GRID_SIZE, MARGIN + y * GRID_SIZE), 5)

    # 显示获胜信息
    if game_state['game_over'] and game_state['winner']:
        text = f"{game_state['winner']} 获胜!"
        text_surface = font.render(text, True, BLUE)
        text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 - 50))
        screen.blit(text_surface, text_rect)

    # 绘制重新开始按钮
    mouse_pos = pygame.mouse.get_pos()
    button_color = BUTTON_HOVER_COLOR if restart_button.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, button_color, restart_button, border_radius=5)
    pygame.draw.rect(screen, BLACK, restart_button, 2, border_radius=5)  # 边框

    text_surface = button_font.render("重新开始", True, WHITE)
    text_rect = text_surface.get_rect(center=restart_button.center)
    screen.blit(text_surface, text_rect)