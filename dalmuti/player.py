from .card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards_played = []
        self.initial_cards = []
        self.cards_remaining = []

    def add_card(self, card: Card) -> None:
        self.initial_cards.append(card)
        self.cards_remaining.append(card)

    def __repr__(self) -> str:
        return f"Player {self.name}, num cards: {len(self.cards_remaining)}, cards remaining: {self.cards_remaining}"
