import ai
import algo

# State 0
the_board = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]

# State 1
the_board = ["_", "_", "_",
             "_", "X", "_",
             "_", "_", "O"]

the_board = ["X", "_", "_",
             "_", "_", "_",
             "_", "_", "O"]

# State 2
the_board = ["_", "_", "X",
             "_", "X", "_",
             "O", "_", "O"]

# the_board = ["X", "O", "X",
#              "_", "_", "_",
#              "_", "_", "O"]

# State 3
# the_board = ["_", "X", "X",
#              "_", "X", "_",
#              "O", "O", "O"]

# the_board = ["X", "O", "X",
#              "O", "_", "_",
#              "X", "_", "O"]

# State 4
# the_board = ["_", "X", "X",
#              "O", "X", "X",
#              "O", "O", "O"]

# the_board = ["X", "X", "_",
#              "O", "O", "_",
#              "X", "_", "_"]

the_player = "X"

ai_value = ai.pick_space_on_board(the_board, the_player)
print(ai_value)

algo_value = algo.pick_space_on_board(the_board)
print(algo_value)
