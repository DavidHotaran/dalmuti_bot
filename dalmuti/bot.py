from .player import Player


class Bot(Player):
    def __init__(self) -> None:
        super().__init__(name="Bot")
        self.seen = {
            i: 0 for i in range(1, 14)
        }  # to keep track of total # of cards played so far
