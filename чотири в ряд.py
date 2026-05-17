import pygame
import sys


WIDTH = 700
HEIGHT = 650

ROWS = 6
COLS = 7

CELL_SIZE = 100
RADIUS = 40

BLUE = (0, 150, 255)
WHITE = (240, 240, 240)
RED = (255, 0, 0)
YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)

player = 1

board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

font = pygame.font.SysFont("Arial", 40)



def draw_board():
    screen.fill(WHITE)


    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 100))


    if player == 1:
        pygame.draw.circle(screen, RED, (50, 50), RADIUS)
    else:
        pygame.draw.circle(screen, YELLOW, (50, 50), RADIUS)


    pygame.draw.rect(screen, BLUE, (0, 100, WIDTH, HEIGHT))


    for row in range(ROWS):
        for col in range(COLS):

            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2 + 100

            color = WHITE

            if board[row][col] == 1:
                color = RED

            elif board[row][col] == 2:
                color = YELLOW

            pygame.draw.circle(screen, color, (x, y), RADIUS)

    pygame.display.update()


def drop_piece(col, current_player):

    for row in range(ROWS - 1, -1, -1):

        if board[row][col] == 0:
            board[row][col] = current_player
            return True

    return False


def check_winner(player_num):


    for row in range(ROWS):
        for col in range(COLS - 3):

            if (
                board[row][col] == player_num and
                board[row][col + 1] == player_num and
                board[row][col + 2] == player_num and
                board[row][col + 3] == player_num
            ):
                return True


    for row in range(ROWS - 3):
        for col in range(COLS):

            if (
                board[row][col] == player_num and
                board[row + 1][col] == player_num and
                board[row + 2][col] == player_num and
                board[row + 3][col] == player_num
            ):
                return True


    for row in range(ROWS - 3):
        for col in range(COLS - 3):

            if (
                board[row][col] == player_num and
                board[row + 1][col + 1] == player_num and
                board[row + 2][col + 2] == player_num and
                board[row + 3][col + 3] == player_num
            ):
                return True


    for row in range(3, ROWS):
        for col in range(COLS - 3):

            if (
                board[row][col] == player_num and
                board[row - 1][col + 1] == player_num and
                board[row - 2][col + 2] == player_num and
                board[row - 3][col + 3] == player_num
            ):
                return True

    return False


def show_winner(text, color):

    label = font.render(text, True, color)

    screen.blit(label, (200, 20))

    pygame.display.update()

    pygame.time.wait(3000)




draw_board()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x = event.pos[0]

            col = mouse_x // CELL_SIZE

            if col < COLS:

                if drop_piece(col, player):

                    draw_board()


                    if check_winner(player):

                        if player == 1:
                            show_winner("Red Wins!", RED)
                        else:
                            show_winner("Yellow Wins!", YELLOW)

                        running = False


                    if player == 1:
                        player = 2
                    else:
                        player = 1

pygame.quit()
sys.exit()