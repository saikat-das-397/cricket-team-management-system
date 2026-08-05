from models.team import Team
from models.player import Player
from models.team_report import TeamReport


class Analytics:
    """
    Provides statistical analysis for a cricket team.

    Responsibilities:
    -----------------
    - Team statistics
    - Player rankings
    - Performance analysis
    - Generate team report

    This class NEVER modifies player data.
    """

    def __init__(self, team: Team):
        self.__team = team

    # ==========================================
    # Private Helper
    # ==========================================

    def _players(self) -> list[Player]:
        """
        Returns a list of all players.
        """
        return list(self.__team)

    # ==========================================
    # Basic Statistics
    # ==========================================

    def get_total_runs(self) -> int:
        return sum(player.get_runs() for player in self.__team)

    def get_total_balls(self) -> int:
        return sum(player.get_balls() for player in self.__team)

    def get_average_runs(self) -> float:

        if len(self.__team) == 0:
            return 0.0

        return round(
            self.get_total_runs() / len(self.__team),
            2
        )

    def get_average_strike_rate(self) -> float:

        if len(self.__team) == 0:
            return 0.0

        average = sum(
            player.strike_rate()
            for player in self.__team
        ) / len(self.__team)

        return round(average, 2)

    # ==========================================
    # Player Rankings
    # ==========================================

    def get_highest_scorer(self) -> Player | None:

        players = self._players()

        if not players:
            return None

        return max(
            players,
            key=lambda player: player.get_runs()
        )

    def get_lowest_scorer(self) -> Player | None:

        players = self._players()

        if not players:
            return None

        return min(
            players,
            key=lambda player: player.get_runs()
        )

    def get_best_strike_rate_player(self) -> Player | None:

        players = self._players()

        if not players:
            return None

        return max(
            players,
            key=lambda player: player.strike_rate()
        )

    def get_top_three_players(self) -> list[Player]:

        return sorted(
            self.__team,
            key=lambda player: player.get_runs(),
            reverse=True
        )[:3]

    # ==========================================
    # Team Report
    # ==========================================

    def generate_report(self) -> TeamReport:

        highest = self.get_highest_scorer()
        lowest = self.get_lowest_scorer()

        return TeamReport(

            total_players=len(self.__team),

            total_runs=self.get_total_runs(),

            total_balls=self.get_total_balls(),

            average_runs=self.get_average_runs(),

            average_strike_rate=self.get_average_strike_rate(),

            highest_scorer=highest,

            lowest_scorer=lowest

        )

    # ==========================================
    # Display
    # ==========================================

    def __str__(self) -> str:
        return f"Analytics({self.__team.get_team_name()})"