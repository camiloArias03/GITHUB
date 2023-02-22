from flask import current_app


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def draw_board(board):
  print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
  print('---------')
  print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
  print('---------')
  print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def get_move(player):
  while True:
    move = input(f'{player}, ingrese su movimiento (fila columna): ')
    try:
      row = int(move[0]) - 1
      col = int(move[2]) - 1
      if row in [0, 1, 2] and col in [0, 1, 2]:
        if board[row][col] == ' ':
          board[row][col] = player
          return
        else:
          print('Esa posición ya está ocupada, intenta otra vez.')
      else:
        print('Posición inválida, intenta otra vez.')
    except (ValueError, IndexError):
      print('Entrada inválida, intenta otra vez.')

def has_won(player):
  # Comprobar filas
  for row in board:
    if row == [player, player, player]:
      return True
  # Comprobar columnas
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # Comprobar diagonales
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def main():
  current_app
