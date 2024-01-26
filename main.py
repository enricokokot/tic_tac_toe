from enum import Enum
import pygame
import random
import time
import tkinter

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
GameStatus = Enum("GameStatus", ["ONGOING", "WINNER", "DRAW"])
PlayerType = Enum("PlayerType", ["HUMAN", "AI"])

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

def check_game_status(board):
  if (board[0][2] == board[1][2] == board[2][2] != Polje.NONE or
      board[3][2] == board[4][2] == board[5][2] != Polje.NONE or 
      board[6][2] == board[7][2] == board[8][2] != Polje.NONE or
      board[0][2] == board[3][2] == board[6][2] != Polje.NONE or
      board[1][2] == board[4][2] == board[7][2] != Polje.NONE or 
      board[2][2] == board[5][2] == board[8][2] != Polje.NONE or
      board[0][2] == board[4][2] == board[8][2] != Polje.NONE or
      board[2][2] == board[4][2] == board[6][2] != Polje.NONE):
    return GameStatus.WINNER
  is_board_not_full = [status_polja[2] for status_polja in board if status_polja[2] == Polje.NONE]
  if not is_board_not_full:
    return GameStatus.DRAW
  return GameStatus.ONGOING

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

def set_current_player(player_types, player_turn):
  if player_turn:
    return player_types[0]
  return player_types[1]

def declare_winner(player_turn):
  if player_turn:
    winner = "O"
  else:
    winner = "X"
  print(f"Good job, {winner} won!")

def main():
  root = tkinter.Tk()
  root.eval('tk::PlaceWindow . center')

  label_0 = tkinter.Label(root)
  label_0.config(text="Who is player 1?")
  label_0.pack()

  player_one_type = tkinter.IntVar()
  R0 = tkinter.Radiobutton(root, text="Human", variable=player_one_type, value=0)
  R0.pack(anchor=tkinter.W)
  R1 = tkinter.Radiobutton(root, text="AI", variable=player_one_type, value=1)
  R1.pack(anchor=tkinter.W)

  label_1 = tkinter.Label(root)
  label_1.config(text="Who is player 2?")
  label_1.pack()
  
  player_two_type = tkinter.IntVar()
  R2 = tkinter.Radiobutton(root, text="Human", variable=player_two_type, value=0)
  R2.pack(anchor=tkinter.W)
  R3 = tkinter.Radiobutton(root, text="AI", variable=player_two_type, value=1)
  R3.pack(anchor=tkinter.W)

  root.mainloop()

  ploca = initialize_game()
  game_over = False
  current_game_status = GameStatus.ONGOING
  figures = []
  player_turn = True
  player_types = [PlayerType.HUMAN, PlayerType.HUMAN]
  if player_one_type.get() == 1:
    player_types[0] = PlayerType.AI
  if player_two_type.get() == 1:
    player_types[1] = PlayerType.AI
  clock = pygame.time.Clock()
  running = True
  while running:
    clock.tick(FPS)
    current_player_type = set_current_player(player_types, player_turn)
    if current_player_type == PlayerType.AI:
      polje_not_found = True
      while polje_not_found:
        player_turn = not player_turn
        x, y = decide_next_step(ploca, player_turn, WIDTH, HEIGHT)
        for polje in ploca:
          if x < polje[0] and y < polje[1]:
            if polje[2] != Polje.NONE:
              player_turn = not player_turn
              print("Polje already taken!")
              break
            elif player_turn:
              polje[2] = Polje.X
            else:
              polje[2] = Polje.O
            time.sleep(2)
            figures.append([polje[0] - WIDTH * 0.16, polje[1] - HEIGHT * 0.16, player_turn])
            break
        current_game_status = check_game_status(ploca)
        if current_game_status == GameStatus.DRAW:
          print("Game Over, nobody won!")
          game_over = True
        elif current_game_status == GameStatus.WINNER:
          game_over = True
          declare_winner(player_turn)
        polje_not_found = False

    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        player_turn = not player_turn
        x, y = pygame.mouse.get_pos()
        for polje in ploca:
          if x < polje[0] and y < polje[1]:
            if polje[2] != Polje.NONE:
              player_turn = not player_turn
              print("Polje already taken!")
              break
            elif player_turn:
              polje[2] = Polje.X
            else:
              polje[2] = Polje.O
            figures.append([polje[0] - WIDTH * 0.16, polje[1] - HEIGHT * 0.16, player_turn])
            break
        current_game_status = check_game_status(ploca)
        if current_game_status == GameStatus.DRAW:
          print("Game Over, nobody won!")
          game_over = True
        elif current_game_status == GameStatus.WINNER:
          declare_winner(player_turn)
          game_over = True

    draw_window(figures)

    if game_over:
      time.sleep(5)
      pygame.quit()

  pygame.quit()

def decide_next_step(ploca, player_turn, WIDTH, HEIGHT):
  polje_not_found = True
  while polje_not_found:
      # TODO: implement next step decision based on current game status
      x, y = random.randrange(WIDTH), random.randrange(HEIGHT)
      for polje in ploca:
          if x < polje[0] and y < polje[1]:
            if polje[2] != Polje.NONE:
              break
            polje_not_found = False
  return x, y

if __name__ == "__main__":
  main()