from . import DisplaySuper


class DisplayDrawer(DisplaySuper.Display):
    def __init__(self, screen, client):
        super().__init__(screen, client)
        self.word = ""

    def update_board(self, word):
        super().update_field(word)
