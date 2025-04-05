import pygame
import sys
from pygame.locals import *
from init import *
from draw import draw_board
from logic import player_move, reset_game

def main():
    """主游戏循环"""
    game_state = init_game()
    reset_game(game_state)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # 检查重新开始按钮
                if game_state['restart_button'].collidepoint(mouse_x, mouse_y):
                    reset_game(game_state)
                # 检查棋盘点击
                elif not game_state['game_over'] and game_state['current_player'] == 2 and mouse_y < WINDOW_SIZE:
                    x = round((mouse_x - MARGIN) / GRID_SIZE)
                    y = round((mouse_y - MARGIN) / GRID_SIZE)
                    if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                        player_move(game_state, x, y)

        draw_board(game_state)
        pygame.display.update()

if __name__ == "__main__":
    main()