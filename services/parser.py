import re

from models.batsman import Batsman
from models.player import Player


class ScorecardParser:
    """
    Reads and writes cricket scorecards.
    """

    PATTERN = re.compile(
        r"^([A-Za-z][A-Za-z ]*)\s+(\d+)\((\d+)\)$"
    )

    # ==========================================
    # Read File
    # ==========================================

    def read_file(self, filename: str) -> list[Player]:
        """
        Read scorecard and return a list of players.
        """

        players = []

        with open(filename, "r") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                match = self.PATTERN.fullmatch(line)

                if not match:
                    print(
                        f"Warning: Invalid record "
                        f"on line {line_number}"
                    )
                    continue

                player = Batsman(

                    match.group(1).strip(),

                    int(match.group(2)),

                    int(match.group(3))

                )

                players.append(player)

        return players

    # ==========================================
    # Save File
    # ==========================================

    def save_file(
        self,
        filename: str,
        players: list[Player]
    ) -> None:
        """
        Save players to scorecard file.
        """

        with open(filename, "w") as file:

            for player in players:

                file.write(

                    f"{player.get_name()} "

                    f"{player.get_runs()}"

                    f"({player.get_balls()})\n"

                )

class InvalidScorecardError(Exception):
    """Raised when a scorecard contains invalid records."""