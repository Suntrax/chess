import math
import pygame
import backend

WIDTH, HEIGHT = 8*128, 8*128
PLAYER_1_COLOR = (225, 225, 225)
PLAYER_2_COLOR = (30, 30, 30)
SELECTED_COLOR = (30, 100, 30)
POSSIBLE_MOVE_COLOR = (150, 30, 30)
POSSIBLE_MOVE_SIZE = 16
CELLS = 8
SELECTION_SIZE = 10

BLACK_PAWN = pygame.image.load('pieces/black-pawn.png')
BLACK_BISHOP = pygame.image.load('pieces/black-bishop.png')
BLACK_KNIGHT = pygame.image.load('pieces/black-knight.png')
BLACK_ROOK = pygame.image.load('pieces/black-rook.png')
BLACK_QUEEN = pygame.image.load('pieces/black-queen.png')
BLACK_KING = pygame.image.load('pieces/black-king.png')

WHITE_PAWN = pygame.image.load('pieces/white-pawn.png')
WHITE_BISHOP = pygame.image.load('pieces/white-bishop.png')
WHITE_KNIGHT = pygame.image.load('pieces/white-knight.png')
WHITE_ROOK = pygame.image.load('pieces/white-rook.png')
WHITE_QUEEN = pygame.image.load('pieces/white-queen.png')
WHITE_KING = pygame.image.load('pieces/white-king.png')

def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
    icon = pygame.image.load('pieces/black-pawn.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    running = True
    board = backend.Board()
    cell_color = PLAYER_1_COLOR
    selected_x, selected_y = None, None
    selected_piece = None
    possible_moves = []
    moved_piece = False
    pygame.mixer.init()
    pygame.mixer.music.load('audio/Gary B.B. Coleman - The Sky is Crying.ogg')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    board_x = mouse_x // (WIDTH // CELLS)
                    board_y = mouse_y // (HEIGHT // CELLS)

                    if selected_piece:
                        moved_piece = board.move_piece(board_x, board_y)

                    if not moved_piece:
                        selected_piece = board.board[board_y][board_x]
                        selected_x = board_x
                        selected_y = board_y
                        possible_moves = board.possible_moves(selected_piece, selected_x, selected_y)

                if event.button == 3:
                    selected_x = None
                    selected_y = None
                    selected_piece = None

        screen.fill("purple")

        for idx_y, y in enumerate(board.board):
            cell_color = PLAYER_1_COLOR if cell_color == PLAYER_2_COLOR else PLAYER_2_COLOR
            for idx_x, x in enumerate(y):
                cell_color = PLAYER_1_COLOR if cell_color == PLAYER_2_COLOR else PLAYER_2_COLOR
                pygame.draw.rect(screen, cell_color, pygame.Rect(idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS, WIDTH/CELLS, HEIGHT/CELLS))

                if x == 1:
                    screen.blit(WHITE_PAWN, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == 2:
                    screen.blit(WHITE_BISHOP, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == 3:
                    screen.blit(WHITE_KNIGHT, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == 4:
                    screen.blit(WHITE_ROOK, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == 5:
                    screen.blit(WHITE_QUEEN, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == 6:
                    screen.blit(WHITE_KING, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))

                elif x == -1:
                    screen.blit(BLACK_PAWN, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == -2:
                    screen.blit(BLACK_BISHOP, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == -3:
                    screen.blit(BLACK_KNIGHT, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == -4:
                    screen.blit(BLACK_ROOK, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == -5:
                    screen.blit(BLACK_QUEEN, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))
                elif x == -6:
                    screen.blit(BLACK_KING, (idx_x*WIDTH/CELLS, idx_y*HEIGHT/CELLS))

        if pygame.mouse.get_pressed()[2]:
            selected_x = None
            selected_y = None
            selected_piece = None

        if selected_piece:
            pygame.draw.rect(screen, SELECTED_COLOR,
                             pygame.Rect(selected_x * WIDTH / CELLS, selected_y * HEIGHT / CELLS, WIDTH / CELLS,
                                         HEIGHT / CELLS), SELECTION_SIZE)
            if possible_moves:
                for move in possible_moves:
                    possible_x = move[0] * WIDTH / CELLS
                    possible_y = move[1] * HEIGHT / CELLS

                    possible_x += math.ceil(WIDTH / CELLS / 2)
                    possible_y += math.ceil(HEIGHT / CELLS / 2)

                    pygame.draw.circle(screen, "black", (possible_y, possible_x), POSSIBLE_MOVE_SIZE + 1)
                    pygame.draw.circle(screen, POSSIBLE_MOVE_COLOR, (possible_y, possible_x), POSSIBLE_MOVE_SIZE)

        if moved_piece:
            selected_x = None
            selected_y = None
            selected_piece = None
            possible_moves = []
            moved_piece = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
