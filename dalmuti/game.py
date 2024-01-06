from .card import Card
from .player import Player
from .bot import Bot
import random


class Game:
    def __init__(self, num_players: int) -> None:
        self.num_players = num_players  # one of the players will be the bot
        self.cards_played = {
            i: 0 for i in range(1, 14)
        }  # to keep track of total # of cards played so far
        self.cards = {i: i * 1 if i != 13 else 2 for i in range(1, 14)}

    def __repr__(self) -> str:
        return (
            f"Num of players: {self.num_players}, \n cards played: ${self.cards_played}"
        )

    def start(self) -> None:
        self.setup()

    def setup(self) -> None:
        """TODO:
        1. Generate the deck of cards for each player (make sure each card is accounted for and there are no extras)
        2. Start while loop
        3. Players take turn according to the rules of the game.
        4. Bot makes choices given probabilites.
        """
        TOTAL_CARDS = 80
        players = [Player(name=f"Player_{i}") for i in range(self.num_players)]
        players.append(Bot())
        player = 0  # who to deal to

        for _ in range(TOTAL_CARDS):
            # we want to continue choosing if we choose a card that has been delt already
            while True:
                card, value = random.choice(list(self.cards.items()))
                if value <= 0:
                    continue
                else:
                    players[player].add_card(Card(value=card))
                    self.cards[card] = value - 1
                    player = 0 if player > self.num_players - 1 else player + 1
                    break
        for player in players:
            print(player)
