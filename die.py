from random import randint

class Die():
    """Klasa przedstawiająca pojedyńczą kość do gry."""

    def __init__(self, num_sides=6):
        """Przyjęcie załozenia, ze kość do gry ma 6 ścian."""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartości z zakresu od 1 do liczby ścian, które ma kostka."""
        return randint(1, self.num_sides)

