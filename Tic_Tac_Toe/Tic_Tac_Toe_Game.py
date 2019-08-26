import Player as p

class Tic_Tac_Toe_Game:

    POS_GAME_MODES = [-1, 1] #List of possible game types.
                                #-1 = end game
                                #1 = Human_Player vs Human_player2
    board = [] #board to represent the tic_tac_toe board


    #Constructor that requires input for game type selection and player
    def __init__(self, selection, Player1, Player2 = None):

        self.game_mode = selection
        self.p1 = Player1
        self.p2 = Player2

        self.start_game()


    #Function that handles the game_mode selection and starts the appropriate
    #game mode.
    def start_game(self):

        while(True):
            
            if self.game_mode == 1:

                print("\nStarting a new two player round...")
                self.play_two_player()

            elif self.game_mode == -1:
                print("Thank you for playing Preston's basic Tic Tac Toe Game!")
                print("***Game Closed***")
                break

            else:
                print("Game has terminated due to a invalid selection of a game mode.")
                break


    def play_two_player(self):

        turn = 1
        winner = None
        active_player = None
        self.board = [1,2,3,4,5,6,7,8,9]
        self.print_game_board()

        while(turn != 10):

            print("Turn #" + str(turn))
        

            if(turn % 2 == 0):
                print(self.p1.get_name() + "\'s turn." )
                active_player = self.p1
            else:
                print(self.p2.get_name() + "\'s turn." )
                active_player = self.p2

            while(True):
                pos = input("Please input a valid move: ")
                try:
                    pos = int(pos)
                except ValueError:
                    print("Invalid move detected. Must be a single digit 1-9 that is not already occupied on the board.")
                    continue

                valid = self.make_move(pos, active_player)
                if(valid == True):
                    break

            self.print_game_board()


            #Check if either player won
            if(self.check_win(self.p1)):
                print(self.p1.get_name() + "Wins!")
                winner = self.p1
                break
            if(self.check_win(self.p2)):
                print(self.p2.get_name() + "Wins!")
                winner = self.p2
                break
        
            turn += 1

        if(winner == None):
            print("Tie game!")
        print("End of Round.")
        self.game_mode = self.play_again()
        


    def play_again(self):

        while(True):
            inp = input("Would you like to play another round? (Y/N): ")
            if(inp == "Y"):
                print("\n")
                return self.game_mode
                
            elif(inp == "N"):
                print("\n")
                return -1
                
            else:
                print("Invalid input, respond \"Y\" for yes or \"N\" for no.")
                continue




    #Validates and makes a chosen move.
    def make_move(self, pos, player):

        #If Position is on board play
        if pos in self.board:
            self.board[pos - 1] = player.get_symbol()
        else:
            print("Invalid Move, given position is not on the board.")
            return False
        return True


    #Print function that prints the tic_tac_Toe game board in its current state.
    def print_game_board(self):

        row = ""

        for i in range(len(self.board)):
            
            row += " " + str(self.board[i]) + " "

            if i % 3 == 2:

                print(row)

                if i != len(self.board) - 1:
                    print("-----------")

                row = ""
            else:
                row += "|"


    #Checks all win possibilities
    def check_win(self, player):
        sym = player.get_symbol()

        if self.board[0] == sym and self.board[1] == sym and self.board[2] == sym:
            return True
        elif self.board[3] == sym and self.board[4] == sym and self.board[5] == sym:
            return True
        elif self.board[6] == sym and self.board[7] == sym and self.board[8] == sym:
            return True
        elif self.board[0] == sym and self.board[3] == sym and self.board[6] == sym:
            return True
        elif self.board[1] == sym and self.board[4] == sym and self.board[7] == sym:
            return True
        elif self.board[2] == sym and self.board[5] == sym and self.board[8] == sym:
            return True
        elif self.board[0] == sym and self.board[4] == sym and self.board[8] == sym:
            return True
        elif self.board[2] == sym and self.board[4] == sym and self.board[6] == sym:
            return True
        else:
            return False


