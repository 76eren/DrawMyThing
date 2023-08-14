class StaticDrawnThings:
    draw_coordinates = []  # Keeps track of all the drawn coordinates, so we can constantly redraw the board
    chat_history = []  # Keeps track of the chat history (what a shocker)
    current_display_item = ""  # Keeps track of the text that is supposed to be displayed at the top
    text = ""  # Keeps track of what is currently being written
    typed_message = ""  # Keeps track of the last message that was typed
    text_to_be_displayed = ""  # Keeps track of the text that is to be displayed at the top when playing the game

