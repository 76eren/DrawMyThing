from . import DisplaySuper


class DisplayGuesser(DisplaySuper.Display):
    def __init__(self, screen, client):
        super().__init__(screen, client)
        self.word_length = None

    def update_board(self, word_length):
        self.word_length = int(word_length)

        wrd = ""
        for i in range(self.word_length):
            wrd += "_"

        super().update_field(wrd)
