import random
import threading


class Controller:
    def __init__(self, room, players: list, server):
        self.room = room
        self.players = players
        self.turn_of_player = 1  # p1 starts first
        self.word = self.assign_word()
        self.server = server
        self.time_per_round_in_seconds = 80
        self.word = None
        self.drawn_coordinates = []  # This is going to be an array containing tuples that represent coordinates

        # Now we create a list with the order of turns
        self.rounds = 2
        self.order_of_turns = []

        for i in range(self.rounds):
            for player in self.players:
                self.order_of_turns.append(player)

    def assign_word(self):
        with open("words.txt", "r") as file:
            words = file.readlines()
            word = random.choice(words).strip().upper()
            return word

    # True = correct gues, don't forward message to other clients in lobby
    # False = incorrect guess, forward message to other clients in lobby
    def check_guess(self, guess: str):
        if guess.upper() == self.word.upper():
            return True
        else:
            return False

    '''
    This function sends all the necessary data to all the clients
    It lets the clients know if it is their turn or not
    This function also sends the word to the client who is drawing
        # Format to drawer: "Yourturn_word"
        # Format to guesser: "Notyourturn_lentghOfWord"
    '''

    def setup_turn(self):
        self.word = self.assign_word()
        for player in self.players:
            if player == self.order_of_turns[0]:  # First player in list is always the drawer
                self.server.send_reply_to_client(f"Yourturn_{self.word}", player)
            else:
                self.server.send_reply_to_client(f"Notyourturn_{len(self.word)}", player)

    def next_turn(self):
        self.order_of_turns.remove(0)

    def timer(self):
        pass
