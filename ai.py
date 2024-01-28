import numpy as np
import pickle

BOARD_ROWS = 3
BOARD_COLS = 3

exp_rate = 0
player_symbol = 1

def play_ai(current_board, player_symbol, states_value):
    positions = availablePositions(current_board)
    chosen_action = chooseAction(exp_rate, states_value, positions, current_board, player_symbol)
    return chosen_action

def availablePositions(board):
    positions = []
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i, j] == 0:
                positions.append((i, j))  # need to be tuple
    return positions

def chooseAction(exp_rate, states_value, positions, current_board, symbol):
    if np.random.uniform(0, 1) <= exp_rate:
        # take random action
        idx = np.random.choice(len(positions))
        action = positions[idx]
    else:
        value_max = -999
        for p in positions:
            next_board = current_board.copy()
            next_board[p] = symbol
            next_boardHash = getHash(next_board)
            value = (
                0
                if states_value.get(next_boardHash) is None
                else states_value.get(next_boardHash)
            )
            # print("value", value)
            if value >= value_max:
                value_max = value
                action = p
    # print("{} takes action {}".format(self.name, action))
    return action

def getHash(board):
    boardHash = str(board.reshape(BOARD_COLS * BOARD_ROWS))
    return boardHash

def loadPolicy(file):
        fr = open(file, "rb")
        states_value = pickle.load(fr)
        fr.close()
        return states_value

def pick_space_on_board(board, player_symbol):
    localized_board = transform_input(board)
    states_value = (loadPolicy("policies/policy_p1")
                    if player_symbol == "X"
                    else loadPolicy("policies/policy_p2"))
    solution = play_ai(localized_board, 1, states_value)
    final_solution = transform_output(solution)
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
        modified_board = [-1. if cell == "X" else cell for cell in board]
        new_board = [1. if cell == "O" else cell for cell in modified_board]
    elif x_plays:
        modified_board = [-1. if cell == "O" else cell for cell in board]
        new_board = [1. if cell == "X" else cell for cell in modified_board]

    finished_board = [0. if cell == "_" else cell for cell in new_board]
    reshaped_board = np.reshape(finished_board, (3, 3))
    return reshaped_board

def transform_output(local_solution):
    final_output = local_solution[0]*3 + local_solution[1]
    return final_output
