from enum import Enum
import pygame

WIDTH, HEIGHT = 300, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT + 50))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDING = 30
RECTANGLE = (PADDING, PADDING, WIDTH - 2*PADDING , HEIGHT - 2*PADDING)
CROSS_SIZE = 30
LINE_THICKNESS = 5

FPS = 60

Polje = Enum('Polje', ['NONE', 'X', 'O'])

def initialize_game():
  ploca = [
    [0.33, 0.33, Polje.NONE], [0.66, 0.33, Polje.NONE], [1.00, 0.33, Polje.NONE],
    [0.33, 0.66, Polje.NONE], [0.66, 0.66, Polje.NONE], [1.00, 0.66, Polje.NONE],
    [0.33, 1.00, Polje.NONE], [0.66, 1.00, Polje.NONE], [1.00, 1.00, Polje.NONE],
  ]

  for polje in ploca:
    polje[0] = polje[0] * WIDTH
    polje[1] = polje[1] * HEIGHT

  return ploca

def draw_board():
  # pygame.draw.rect(WIN, BLACK, RECTANGLE)

  pygame.draw.lines(WIN, BLACK, True, [(WIDTH*0.33,0),(WIDTH*0.33,HEIGHT)], LINE_THICKNESS - 1)
  pygame.draw.lines(WIN, BLACK, True, [(WIDTH*0.66,0),(WIDTH*0.66,HEIGHT)], LINE_THICKNESS - 1)

  pygame.draw.lines(WIN, BLACK, True, [(0,HEIGHT*0.33),(WIDTH,HEIGHT*0.33)], LINE_THICKNESS - 1)
  pygame.draw.lines(WIN, BLACK, True, [(0,HEIGHT*0.66),(WIDTH,HEIGHT*0.66)], LINE_THICKNESS - 1)

def draw_x(x, y):
  pygame.draw.lines(WIN, BLACK, True, [(x-CROSS_SIZE,y-CROSS_SIZE),(x+CROSS_SIZE,y+CROSS_SIZE)], LINE_THICKNESS)
  pygame.draw.lines(WIN, BLACK, True, [(x-CROSS_SIZE,y+CROSS_SIZE),(x+CROSS_SIZE,y-CROSS_SIZE)], LINE_THICKNESS)

def draw_o(x, y):
  pygame.draw.circle(WIN, BLACK, [x, y], CROSS_SIZE, LINE_THICKNESS)

def draw_window(figures):
  WIN.fill(WHITE)
  draw_board()
  for figure in figures:
    if figure[2] == False:
      draw_x(figure[0], figure[1])
    else:
      draw_o(figure[0], figure[1])
  pygame.display.update()


def main():
  ploca = initialize_game()
  figures = []
  player_turn = True
  clock = pygame.time.Clock()
  running = True
  while running:
    clock.tick(FPS)
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        player_turn = not player_turn
        x, y = pygame.mouse.get_pos()
        for polje in ploca:
          if x < polje[0] and y < polje[1]:
            if polje[2] != Polje.NONE:
              print("Polje already taken!")
              break
            elif player_turn:
              polje[2] = Polje.X
            else:
              polje[2] = Polje.O
            figures.append([polje[0] - WIDTH * 0.16, polje[1] - HEIGHT * 0.16, player_turn])
            break
        # print(ploca)

    draw_window(figures)

  pygame.quit()

if __name__ == "__main__":
  main()