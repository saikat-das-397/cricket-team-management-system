from models.player import Player

class Batsman(Player):

    def __init__(self, name, runs, balls):
        super().__init__(name, runs, balls)

    # Overriding Abstract Method
    def display(self):

        print(
            f"{self.get_name():<25}"
            f"{self.get_runs():<10}"
            f"{self.get_balls():<10}"
            f"{self.strike_rate():.2f}"
        )