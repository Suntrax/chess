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
        self.selected_piece = None
        self.selected_piece_pos = None
        self.possible_moves_list = None
        self.board = board

    def possible_moves(self, piece: int, pos_x: int, pos_y: int) -> list:
        possible_moves_list = []
        if piece == white_pawn:
            if pos_y == 6:
                possible_moves_list.append([pos_y - 2, pos_x])
            if self.board[pos_y - 1][pos_x] == 0:
                possible_moves_list.append([pos_y - 1, pos_x])
            if self.board[pos_y - 1][pos_x - 1] < 0:
                possible_moves_list.append([pos_y - 1, pos_x - 1])
            if self.board[pos_y - 1][pos_x + 1] < 0:
                possible_moves_list.append([pos_y - 1, pos_x + 1])

        if piece == white_bishop:
            moves_top_left = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
            moves_top_right = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
            moves_bottom_left = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
            moves_bottom_right = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

            for move in moves_top_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] <= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

        if piece == white_rook:
            moves_down = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
            moves_left = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
            moves_right = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
            moves_up = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

            for move in moves_down:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] < 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] <= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

        if piece == black_pawn:
            if pos_y == 1:
                possible_moves_list.append([pos_y + 2, pos_x])
            if self.board[pos_y + 1][pos_x] == 0:
                possible_moves_list.append([pos_y + 1, pos_x])
            if self.board[pos_y + 1][pos_x + 1] > 0:
                possible_moves_list.append([pos_y - 1, pos_x - 1])
            if self.board[pos_y + 1][pos_x - 1] > 0:
                possible_moves_list.append([pos_y + 1, pos_x - 1])

        if piece == black_bishop:
            moves_top_left = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
            moves_top_right = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
            moves_bottom_left = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
            moves_bottom_right = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

            for move in moves_top_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_top_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] >= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

        if piece == black_rook:
            moves_down = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
            moves_left = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
            moves_right = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
            moves_up = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

            for move in moves_down:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_top_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_bottom_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_left:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_right:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                        break
                    else:
                        break

            for move in moves_up:
                if -1 < pos_y + move[0] < 8 and -1 < pos_x + move[1] < 8:
                    if board[pos_y + move[0]][pos_x + move[1]] == 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])
                    elif board[pos_y + move[0]][pos_x + move[1]] > 0:
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
                    if board[pos_y + move[0]][pos_x + move[1]] >= 0:
                        possible_moves_list.append([pos_y + move[0], pos_x + move[1]])

        self.possible_moves_list = possible_moves_list
        self.selected_piece_pos = [pos_y, pos_x]
        self.selected_piece = piece
        return possible_moves_list

    def move_piece(self, pos_x: int, pos_y: int) -> bool:
        if [pos_y, pos_x] in self.possible_moves_list:
            self.board[pos_y][pos_x] = self.selected_piece
            self.board[self.selected_piece_pos[0]][self.selected_piece_pos[1]] = 0
            self.possible_moves_list = None
            self.selected_piece = None
            return True
        return False

    def evolve_pawn(self):
        return
