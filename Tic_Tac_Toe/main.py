
import Player as p
import Tic_Tac_Toe_Game as ttt


game_type = 1
p1_sym = "X"
p2_sym = "O"

print("This program initializes a Tic Tac Toe Game.")
print("Player 1 will be X's and Player 2 will be O's")
p1_name = input("Player 1 name: ")
p2_name = input("Player 2 name: ")

p1 = p.Player(p1_name, p1_sym)
p2 = p.Player(p2_name, p2_sym)


ttt.Tic_Tac_Toe_Game(game_type, p1, p2)