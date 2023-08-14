from . import DisplaySuper


class DisplayGuesser(DisplaySuper.Display):
    def __init__(self, board):
        super().__init__(board)
        self.word_length = None
        self.board = board

    def update_board(self, word_length):
        self.word_length = int(word_length)

        wrd = ""
        for i in range(self.word_length):
            wrd += "_"
            wrd += " "

        super().update_field(wrd)
