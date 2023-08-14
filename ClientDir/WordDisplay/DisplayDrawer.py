from . import DisplaySuper


class DisplayDrawer(DisplaySuper.Display):
    def __init__(self, board):
        self.board = board
        super().__init__(board)

    def update_board(self, word):
        super().update_field(word)
