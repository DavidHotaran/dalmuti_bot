class Card:
    def __init__(self, value: int) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f"Card - {self.value}"


