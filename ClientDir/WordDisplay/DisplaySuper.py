from DrawnThingsTracker import StaticDrawnThings  # Pycharm marks this as an error but this works fine actually, silly pycharm being a lil quirky as usual


class Display:
    def __init__(self, board):
        self.board = board

    def update_field(self, word):
        StaticDrawnThings.text_to_be_displayed = word
        self.board.redraw_all()
