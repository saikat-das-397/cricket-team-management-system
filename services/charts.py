import os
import matplotlib.pyplot as plt

from models.team import Team


class ChartService:
    """
    Generates charts for the cricket team.
    """

    OUTPUT_FOLDER = "charts"

    def __init__(self, team: Team):

        self.__team = team

        os.makedirs(
            self.OUTPUT_FOLDER,
            exist_ok=True
        )

    # ==========================================
    # Helpers
    # ==========================================

    def _players(self):

        return list(self.__team)

    def _names(self):

        return [
            player.get_name()
            for player in self.__team
        ]

    def _runs(self):

        return [
            player.get_runs()
            for player in self.__team
        ]

    # ==========================================
    # Runs Chart
    # ==========================================

    def create_runs_chart(self):

        if len(self.__team) == 0:
            return None

        plt.figure(figsize=(10, 5))

        plt.bar(
            self._names(),
            self._runs()
        )

        plt.title("Runs Scored")

        plt.xlabel("Players")

        plt.ylabel("Runs")

        plt.xticks(rotation=20)

        plt.tight_layout()

        filename = os.path.join(
            self.OUTPUT_FOLDER,
            "runs_chart.png"
        )

        plt.savefig(filename)

        plt.close()

        return filename

    # ==========================================
    # Strike Rate Chart
    # ==========================================

    def create_strike_rate_chart(self):

        if len(self.__team) == 0:
            return None

        strike_rates = [

            player.strike_rate()

            for player in self.__team

        ]

        plt.figure(figsize=(10, 5))

        plt.bar(
            self._names(),
            strike_rates
        )

        plt.title("Strike Rate")

        plt.xlabel("Players")

        plt.ylabel("Strike Rate")

        plt.xticks(rotation=20)

        plt.tight_layout()

        filename = os.path.join(

            self.OUTPUT_FOLDER,

            "strike_rate_chart.png"

        )

        plt.savefig(filename)

        plt.close()

        return filename

    # ==========================================
    # Pie Chart
    # ==========================================

    def create_contribution_chart(self):

        if len(self.__team) == 0:
            return None

        plt.figure(figsize=(7, 7))

        plt.pie(

            self._runs(),

            labels=self._names(),

            autopct="%1.1f%%",

            startangle=90

        )

        plt.title(
            "Team Run Contribution"
        )

        filename = os.path.join(

            self.OUTPUT_FOLDER,

            "team_contribution.png"

        )

        plt.savefig(filename)

        plt.close()

        return filename

    # ==========================================
    # Horizontal Ranking
    # ==========================================

    def create_ranking_chart(self):

        if len(self.__team) == 0:
            return None

        players = sorted(

            self.__team,

            key=lambda p: p.get_runs(),

            reverse=True

        )

        names = [
            p.get_name()
            for p in players
        ]

        runs = [
            p.get_runs()
            for p in players
        ]

        plt.figure(figsize=(8, 5))

        plt.barh(names, runs)

        plt.title(
            "Player Ranking"
        )

        plt.tight_layout()

        filename = os.path.join(

            self.OUTPUT_FOLDER,

            "ranking.png"

        )

        plt.savefig(filename)

        plt.close()

        return filename

    # ==========================================
    # Generate All
    # ==========================================

    def generate_all_charts(self):

        return {

            "Runs":

                self.create_runs_chart(),

            "Strike Rate":

                self.create_strike_rate_chart(),

            "Contribution":

                self.create_contribution_chart(),

            "Ranking":

                self.create_ranking_chart()

        }