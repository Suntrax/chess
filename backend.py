import copy
import random

board = [
    [-4,-3,-2,-5,-6,-2,-3,-4],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [4,3,2,5,6,2,3,4],
]

default_board = [
    [-4,-3,-2,-5,-6,-2,-3,-4],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [4,3,2,5,6,2,3,4],
]

white_pawn = 1
white_bishop = 2
white_knight = 3
white_rook = 4
white_queen = 5
white_king = 6

black_pawn = -1
black_bishop = -2
black_knight = -3
black_rook = -4
black_queen = -5
black_king = -6

class Board:
    def __init__(self):
        self.available_bot_pieces = None
        self.selected_piece = None
        self.selected_piece_pos = None
        self.possible_moves_list = None
        self.board = board
        self.available_bot_moves = None
        self.previous_moves_list = []
        self.en_passant_target = None
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_rooks_moved = {"left": False, "right": False}
        self.black_rooks_moved = {"left": False, "right": False}

    def possible_moves(self, piece: int, pos_x: int, pos_y: int, check_for_safety = True) -> list:
        possible_moves_list = []
        if piece == white_pawn:
            if pos_y == 6 and board[pos_y-2][pos_x] == 0:
                possible_moves_list.append([pos_y - 2, pos_x])
            if self.board[pos_y - 1][pos_x] == 0:
                possible_moves_list.append([pos_y - 1, pos_x])
            if pos_x + 1 < 8:
                if self.board[pos_y - 1][pos_x + 1] < 0:
                    possible_moves_list.append([pos_y - 1, pos_x + 1])
            if pos_x - 1 > -1:
                if self.board[pos_y - 1][pos_x - 1] < 0:
                    possible_moves_list.append([pos_y - 1, pos_x - 1])
            if self.en_passant_target:
                target_y, target_x = self.en_passant_target
                if pos_y - 1 == target_y and abs(pos_x - target_x) == 1:
                    possible_moves_list.append([target_y, target_x])

        if piece == white_bishop:
            moves_top_left = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
            moves_top_right = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
            moves_bottom_left = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
            moves_bottom_right = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

            for move in moves_top_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_top_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

        if piece == white_knight:
            moves = [[-2, -1], [-2, 1],
                     [-1, 2], [1, 2],
                     [2, 1], [2, -1],
                     [1, -2], [-1, -2]]

            for move in moves:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] <= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

        if piece == white_rook:
            moves_down = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
            moves_left = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
            moves_right = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
            moves_up = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

            for move in moves_down:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

        if piece == white_queen:
            moves_top_left = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
            moves_top_right = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
            moves_bottom_left = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
            moves_bottom_right = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

            for move in moves_top_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_top_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            moves_down = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
            moves_left = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
            moves_right = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
            moves_up = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

            for move in moves_down:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

        if piece == white_king:
            moves = [[-1, -1], [-1, 0], [-1, 1],
                     [0, -1], [0, 1],
                     [1, -1], [1, 0], [1, 1]]

            for move in moves:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] <= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

            if check_for_safety and not self.white_king_moved and not self.is_in_check("white"):
                # Kingside (Right)
                if not self.white_rooks_moved["right"] and self.board[7][5] == 0 and self.board[7][6] == 0:
                    if not self.is_square_attacked(7, 5, "black") and not self.is_square_attacked(7, 6, "black"):
                        possible_moves_list.append([7, 6])
                # Queenside (Left)
                if not self.white_rooks_moved["left"] and self.board[7][1] == 0 and self.board[7][2] == 0 and \
                        self.board[7][3] == 0:
                    if not self.is_square_attacked(7, 3, "black") and not self.is_square_attacked(7, 2, "black"):
                        possible_moves_list.append([7, 2])

        if piece == black_pawn:
            if pos_y == 1 and board[pos_y+2][pos_x] == 0:
                possible_moves_list.append([pos_y + 2, pos_x])
            if self.board[pos_y + 1][pos_x] == 0:
                possible_moves_list.append([pos_y + 1, pos_x])
            if pos_x + 1 < 8:
                if self.board[pos_y + 1][pos_x + 1] > 0:
                    possible_moves_list.append([pos_y + 1, pos_x + 1])
            if pos_x - 1 > -1:
                if self.board[pos_y + 1][pos_x - 1] > 0:
                    possible_moves_list.append([pos_y + 1, pos_x - 1])
            if self.en_passant_target:
                target_y, target_x = self.en_passant_target
                if pos_y + 1 == target_y and abs(pos_x - target_x) == 1:
                    possible_moves_list.append([target_y, target_x])

        if piece == black_bishop:
            moves_top_left = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
            moves_top_right = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
            moves_bottom_left = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
            moves_bottom_right = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

            for move in moves_top_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_top_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

        if piece == black_knight:
            moves = [[-2, -1], [-2, 1],
                     [-1, 2], [1, 2],
                     [2, 1], [2, -1],
                     [1, -2], [-1, -2]]

            for move in moves:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] >= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

        if piece == black_rook:
            moves_down = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
            moves_left = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
            moves_right = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
            moves_up = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

            for move in moves_down:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

        if piece == black_queen:
            moves_top_left = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
            moves_top_right = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
            moves_bottom_left = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
            moves_bottom_right = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

            for move in moves_top_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_top_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            moves_down = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
            moves_left = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
            moves_right = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
            moves_up = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

            for move in moves_down:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif self.board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

        if piece == black_king:
            moves = [[-1, -1], [-1 ,0], [-1, 1],
                     [0, -1], [0, 1],
                     [1, -1], [1, 0], [1, 1]]

            for move in moves:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if self.board[pos_y + move[0]][pos_x + move[1]] >= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

            if check_for_safety and not self.black_king_moved and not self.is_in_check("black"):
                # Kingside (Right) - Squares [0, 5] and [0, 6] must be empty
                if not self.black_rooks_moved["right"] and self.board[0][5] == 0 and self.board[0][6] == 0:
                    if not self.is_square_attacked(0, 5, "white") and not self.is_square_attacked(0, 6, "white"):
                        possible_moves_list.append([0, 6])

                # Queenside (Left) - Squares [0, 1], [0, 2], and [0, 3] must be empty
                if not self.black_rooks_moved["left"] and self.board[0][1] == 0 and self.board[0][2] == 0 and \
                        self.board[0][3] == 0:
                    if not self.is_square_attacked(0, 3, "white") and not self.is_square_attacked(0, 2, "white"):
                        possible_moves_list.append([0, 2])

        self.possible_moves_list = possible_moves_list
        self.selected_piece_pos = [pos_y, pos_x]
        self.selected_piece = piece

        if check_for_safety:
            safe_moves = []
            for move in possible_moves_list:
                if self.is_move_safe(piece, [pos_y, pos_x], move):
                    safe_moves.append(move)
            self.possible_moves_list = safe_moves
            return safe_moves

        return possible_moves_list

    def move_piece(self, pos_x: int, pos_y: int) -> bool:
        if [pos_y, pos_x] in self.possible_moves_list:
            prev_y, prev_x = self.selected_piece_pos
            current_player_color = "white" if self.selected_piece > 0 else "black"
            enemy_color = "black" if current_player_color == "white" else "white"

            # 1. Handle En Passant Capture (Removing the enemy pawn)
            if (self.selected_piece == white_pawn or self.selected_piece == black_pawn) and \
                    [pos_y, pos_x] == self.en_passant_target:
                # If white captures, the black pawn is below it. If black captures, white is above.
                capture_y = pos_y + 1 if self.selected_piece == white_pawn else pos_y - 1
                self.board[capture_y][pos_x] = 0

            # 2. Handle Rochade (Castling) - Moving the Rook
            # White Castling
            if self.selected_piece == white_king and abs(pos_x - prev_x) == 2:
                if pos_x == 6:  # Kingside
                    self.board[7][5] = white_rook
                    self.board[7][7] = 0
                elif pos_x == 2:  # Queenside
                    self.board[7][3] = white_rook
                    self.board[7][0] = 0

            # Black Castling
            if self.selected_piece == black_king and abs(pos_x - prev_x) == 2:
                if pos_x == 6:  # Kingside
                    self.board[0][5] = black_rook
                    self.board[0][7] = 0
                elif pos_x == 2:  # Queenside
                    self.board[0][3] = black_rook
                    self.board[0][0] = 0

            # 3. Update Movement History (To disable future castling)
            if self.selected_piece == white_king:
                self.white_king_moved = True
            elif self.selected_piece == black_king:
                self.black_king_moved = True

            if self.selected_piece == white_rook:
                if prev_x == 0: self.white_rooks_moved["left"] = True
                if prev_x == 7: self.white_rooks_moved["right"] = True
            elif self.selected_piece == black_rook:
                if prev_x == 0: self.black_rooks_moved["left"] = True
                if prev_x == 7: self.black_rooks_moved["right"] = True

            # 4. Handle Pawn Evolution (Promotion)
            self.evolve_pawn()

            # 5. Execute the Main Move
            self.board[pos_y][pos_x] = self.selected_piece
            self.board[prev_y][prev_x] = 0

            # 6. Set En Passant Target for the NEXT turn
            # If a pawn just moved 2 squares, mark the square behind it as vulnerable
            self.en_passant_target = None
            if abs(pos_y - prev_y) == 2:
                if self.selected_piece == white_pawn or self.selected_piece == black_pawn:
                    self.en_passant_target = [(pos_y + prev_y) // 2, pos_x]

            # 7. Determine enemy game state
            if self.is_checkmate(enemy_color):
                print(f"CHECKMATE! {current_player_color.capitalize()} wins!")
            elif self.is_stalemate(enemy_color):
                print("STALEMATE! It's a draw.")
            elif self.is_in_check(enemy_color):
                print(f"CHECK! {enemy_color.capitalize()} King is under attack!")

            # 8. Reset selection state
            self.possible_moves_list = None
            self.selected_piece = None
            return True

        return False

    def ai_move(self):
        legal_moves = []

        for y in range(8):
            for x in range(8):
                piece = self.board[y][x]
                if piece < 0:
                    moves = self.possible_moves(piece, x, y)
                    for move in moves:
                        legal_moves.append((x, y, move))

        if not legal_moves:
            return

        start_x, start_y, move = random.choice(legal_moves)

        self.possible_moves(self.board[start_y][start_x], start_x, start_y)
        self.move_piece(move[1], move[0])

    def evolve_pawn(self) -> None:
        if self.selected_piece == white_pawn:
            if self.selected_piece_pos[0]-1 == 0:
                self.selected_piece = white_queen
        if self.selected_piece == black_pawn:
            if self.selected_piece_pos[0]+1 == 7:
                self.selected_piece = black_queen

    def find_king(self, king_val):
        for y in range(8):
            for x in range(8):
                if self.board[y][x] == king_val:
                    return [y, x]
        return None

    def is_in_check(self, color):
        if color == "white":
            king_val = white_king
            enemy_is_white = False
        else:
            king_val = black_king
            enemy_is_white = True

        king_pos = self.find_king(king_val)
        if not king_pos:
            return False

        old_selected = self.selected_piece
        old_pos = self.selected_piece_pos
        old_moves = self.possible_moves_list

        in_check = False
        for y in range(8):
            for x in range(8):
                piece = self.board[y][x]
                is_enemy = (enemy_is_white and piece > 0) or (not enemy_is_white and piece < 0)

                if is_enemy:
                    # CRITICAL FIX: Add check_for_safety=False here
                    moves = self.possible_moves(piece, x, y, check_for_safety=False)
                    if king_pos in moves:
                        in_check = True
                        break
            if in_check:
                break

        # Restore state
        self.selected_piece = old_selected
        self.selected_piece_pos = old_pos
        self.possible_moves_list = old_moves

        return in_check

    def is_move_safe(self, piece, start_pos, end_pos):
        temp_board = copy.deepcopy(self.board)
        temp_board[end_pos[0]][end_pos[1]] = piece
        temp_board[start_pos[0]][start_pos[1]] = 0

        original_board = self.board
        self.board = temp_board

        color = "white" if piece > 0 else "black"
        still_in_check = self.is_in_check(color)
        self.board = original_board
        return not still_in_check

    def is_square_attacked(self, y, x, enemy_color):
        original_piece = self.board[y][x]
        self.board[y][x] = white_king if enemy_color == "black" else black_king
        attacked = self.is_in_check("white" if enemy_color == "black" else "black")
        self.board[y][x] = original_piece
        return attacked

    def has_legal_moves(self, color):
        for y in range(8):
            for x in range(8):
                piece = self.board[y][x]

                if color == "white" and piece > 0:
                    moves = self.possible_moves(piece, x, y)
                    if moves:
                        return True

                if color == "black" and piece < 0:
                    moves = self.possible_moves(piece, x, y)
                    if moves:
                        return True

        return False

    def is_checkmate(self, color):
        if self.is_in_check(color) and not self.has_legal_moves(color):
            return True
        return False

    def is_stalemate(self, color):
        if not self.is_in_check(color) and not self.has_legal_moves(color):
            return True
        return False
