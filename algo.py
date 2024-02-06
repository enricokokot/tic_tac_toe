import numpy as np
import json

def minimax(board, player):

    empty_cells = np.argwhere(board == 0)
    if check_winner(board) == 1:
        return -1, -1, 1
    elif check_winner(board) == 2:
        return -1, -1, -1
    elif len(empty_cells) == 0:
        return -1, -1, 0

    moves = []
    # total_moves = len(empty_cells)
    for cell in empty_cells:
        board[cell[0], cell[1]] = player
        score = minimax(board, 3 - player)[2]
        board[cell[0], cell[1]] = 0
        moves.append((cell[0], cell[1], score))

    if player == 1:
        best_move = max(moves, key=lambda x: x[2])
        # for move in moves:
        #     move_prob = (move[2] + 1) / 2
        #     move_percentage = round((move_prob / total_moves) * 100, 2)
        #     print(
        #         f"Move {move[0]}, {move[1]}: Probability of winning = {move_percentage}%")
    else:
        best_move = min(moves, key=lambda x: x[2])

    return best_move

def check_winner(board):

    for i in range(3):
        if all(board[i, j] == 2 for j in range(3)) or all(board[j, i] == 2 for j in range(3)):
            return 2

    if all(board[i, i] == 2 for i in range(3)) or all(board[i, 2 - i] == 2 for i in range(3)):
        return 2

    for i in range(3):
        if all(board[i, j] == 1 for j in range(3)) or all(board[j, i] == 1 for j in range(3)):
            return 1

    if all(board[i, i] == 1 for i in range(3)) or all(board[i, 2 - i] == 1 for i in range(3)):
        return 1

    if np.all(board != 0):
        return 0

    return -1

def pick_space_on_board(board):
    move_picker = read_from_manual()
    hashed_board = str(board)

    if hashed_board in move_picker.keys():
        return move_picker[hashed_board]

    localized_board = transform_input(board)
    solution = minimax(localized_board, 1)
    final_solution = transform_output(solution)

    move_picker[hashed_board] = final_solution
    write_to_manual(move_picker)
    return final_solution

def transform_input(input):
    board = input
    xs = len([x for x in board if x == "X"])
    os = len([o for o in board if o == "O"])

    o_plays = xs-1 == os
    x_plays = xs == os

    if not o_plays and not x_plays:
        return "Error: The given board is corrupted."

    if o_plays:
        modified_board = [2 if cell == "X" else cell for cell in board]
        new_board = [1 if cell == "O" else cell for cell in modified_board]
    elif x_plays:
        modified_board = [2 if cell == "O" else cell for cell in board]
        new_board = [1 if cell == "X" else cell for cell in modified_board]

    finished_board = [0 if cell == "_" else cell for cell in new_board]
    reshaped_board = np.reshape(finished_board, (3, 3))
    return reshaped_board

def transform_output(local_solution):
    final_output = local_solution[0]*3 + local_solution[1]
    return int(final_output)

def read_from_manual():
    with open("manual.txt", "r") as the_file:
        return json.load(the_file)

def write_to_manual(manual):
    json_object = json.dumps(manual, indent=4)
    with open("manual.txt", "w") as the_file:
        the_file.write(json_object)