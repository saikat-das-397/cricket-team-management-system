from models.player import Player


class Batsman(Player):
    """
    Represents a batsman in the cricket team.
    """

    def __init__(self, name: str, runs: int, balls: int):
        super().__init__(name, runs, balls)

    def display(self) -> None:
        """
        Display batsman information in table format.
        """

        print(
            f"{self.get_name():<25}"
            f"{self.get_runs():>8}"
            f"{self.get_balls():>10}"
            f"{self.strike_rate():>15.2f}"
        )