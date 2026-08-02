import os
import matplotlib.pyplot as plt


class ChartService:
    """
    Creates charts from Team data.
    """

    def __init__(self, team):

        self.team = team

        # Automatically create charts folder
        os.makedirs("charts", exist_ok=True)

    # ---------------------------------
    # Runs Bar Chart
    # ---------------------------------
    def create_runs_chart(self):

        players = self.team.get_players()

        if not players:
            print("No data available.")
            return

        names = [player.get_name() for player in players]
        runs = [player.get_runs() for player in players]

        plt.figure(figsize=(10, 5))

        plt.bar(names, runs)

        plt.title("Runs Scored")

        plt.xlabel("Players")

        plt.ylabel("Runs")

        plt.xticks(rotation=20)

        plt.tight_layout()

        plt.savefig("charts/runs_chart.png")

        plt.close()

        print("Runs chart created.")

    # ---------------------------------
    # Strike Rate Chart
    # ---------------------------------
    def create_strike_rate_chart(self):

        players = self.team.get_players()

        if not players:
            print("No data available.")
            return

        names = [player.get_name() for player in players]

        strike_rates = [
            player.strike_rate()
            for player in players
        ]

        plt.figure(figsize=(10, 5))

        plt.bar(names, strike_rates)

        plt.title("Strike Rate Comparison")

        plt.xlabel("Players")

        plt.ylabel("Strike Rate")

        plt.xticks(rotation=20)

        plt.tight_layout()

        plt.savefig("charts/strike_rate_chart.png")

        plt.close()

        print("Strike rate chart created.")

    # ---------------------------------
    # Team Contribution Pie Chart
    # ---------------------------------
    def create_team_contribution_chart(self):

        players = self.team.get_players()

        if not players:
            print("No data available.")
            return

        names = [player.get_name() for player in players]

        runs = [player.get_runs() for player in players]

        plt.figure(figsize=(7, 7))

        plt.pie(
            runs,
            labels=names,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Team Run Contribution")

        plt.tight_layout()

        plt.savefig("charts/team_contribution.png")

        plt.close()

        print("Contribution chart created.")

    # ---------------------------------
    # Generate All Charts
    # ---------------------------------
    def generate_all_charts(self):

        self.create_runs_chart()

        self.create_strike_rate_chart()

        self.create_team_contribution_chart()

        print("\nAll charts generated successfully!")