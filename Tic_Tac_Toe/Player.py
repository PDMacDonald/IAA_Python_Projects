class Player:

    def __init__(self, player_name, symbol):

        self.name = player_name
        self.tic_tac_toe_symbol = symbol

    def set_player_name(self, str_name):
        self.name = str_name

    def get_symbol(self):
        
        return self.tic_tac_toe_symbol
    
    def get_name(self):
        
        return self.name