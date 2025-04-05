import numpy as np
import random
from init import *

def is_valid_move(board, x, y):
    """检查落子是否有效"""
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[y][x] == 0

def check_win(board, x, y, player):
    """检查是否获胜"""
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dx, dy in directions:
        count = 1  # 当前落子

        # 向一个方向检查
        nx, ny = x + dx, y + dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == player:
            count += 1
            nx += dx
            ny += dy

        # 向相反方向检查
        nx, ny = x - dx, y - dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == player:
            count += 1
            nx -= dx
            ny -= dy

        if count >= 5:
            return True
    return False

def evaluate_position(board, x, y, player):
    """评估位置得分"""
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dx, dy in directions:
        line = 1  # 当前棋子
        # 正向检查
        nx, ny = x + dx, y + dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == player:
            line += 1
            nx += dx
            ny += dy
        # 反向检查
        nx, ny = x - dx, y - dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == player:
            line += 1
            nx -= dx
            ny -= dy

        if line >= 5: return 10000  # 胜利
        if line == 4: score += 1000
        elif line == 3: score += 100
        elif line == 2: score += 10
    return score

def find_best_move(board):
    """AI寻找最佳落子位置"""
    if np.sum(board) == 0:  # 第一步下天元
        return (BOARD_SIZE // 2, BOARD_SIZE // 2)

    best_score = -1
    best_move = None
    center = BOARD_SIZE // 2

    for y in range(max(0, center - 3), min(BOARD_SIZE, center + 4)):
        for x in range(max(0, center - 3), min(BOARD_SIZE, center + 4)):
            if is_valid_move(board, x, y):
                score = evaluate_position(board, x, y, 1) + evaluate_position(board, x, y, 2) * 0.8
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    if best_move is None:  # 随机选择
        valid_moves = [(x, y) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE) if is_valid_move(board, x, y)]
        if valid_moves:
            return random.choice(valid_moves)
    return best_move

def computer_move(game_state):
    """电脑走棋"""
    move = find_best_move(game_state['board'])
    if move:
        x, y = move
        game_state['board'][y][x] = 1
        game_state['last_move'] = (x, y)
        if check_win(game_state['board'], x, y, 1):
            game_state['game_over'] = True
            game_state['winner'] = "黑棋(电脑)"
        else:
            game_state['current_player'] = 2

def player_move(game_state, x, y):
    """玩家走棋"""
    if is_valid_move(game_state['board'], x, y):
        game_state['board'][y][x] = 2
        game_state['last_move'] = (x, y)
        if check_win(game_state['board'], x, y, 2):
            game_state['game_over'] = True
            game_state['winner'] = "白棋(玩家)"
        else:
            game_state['current_player'] = 1
            computer_move(game_state)

def reset_game(game_state):
    """重置游戏"""
    game_state['board'] = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    game_state['current_player'] = 1
    game_state['game_over'] = False
    game_state['last_move'] = None
    game_state['winner'] = None
    computer_move(game_state)