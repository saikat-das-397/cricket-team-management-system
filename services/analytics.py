class Analytics:
    """
    Analytics Class

    Responsible for:
    ----------------
    1. Team statistics
    2. Player performance analysis
    3. Rankings
    4. Reports (data only)

    It NEVER modifies player data.
    """

    def __init__(self, team):
        self.team = team

    # -----------------------------------
    # Total Runs
    # -----------------------------------
    def get_total_runs(self):

        players = self.team.get_players()

        if not players:
            return 0

        return sum(player.get_runs() for player in players)

    # -----------------------------------
    # Total Balls
    # -----------------------------------
    def get_total_balls(self):

        players = self.team.get_players()

        if not players:
            return 0

        return sum(player.get_balls() for player in players)

    # -----------------------------------
    # Average Runs
    # -----------------------------------
    def get_average_runs(self):

        players = self.team.get_players()

        if not players:
            return 0

        return round(
            self.get_total_runs() / len(players),
            2
        )

    # -----------------------------------
    # Average Strike Rate
    # -----------------------------------
    def get_average_strike_rate(self):

        players = self.team.get_players()

        if not players:
            return 0

        average = sum(
            player.strike_rate()
            for player in players
        ) / len(players)

        return round(average, 2)

    # -----------------------------------
    # Highest Scorer
    # -----------------------------------
    def get_highest_scorer(self):

        players = self.team.get_players()

        if not players:
            return None

        return max(
            players,
            key=lambda player: player.get_runs()
        )

    # -----------------------------------
    # Lowest Scorer
    # -----------------------------------
    def get_lowest_scorer(self):

        players = self.team.get_players()

        if not players:
            return None

        return min(
            players,
            key=lambda player: player.get_runs()
        )

    # -----------------------------------
    # Top 3 Players
    # -----------------------------------
    def get_top_three_players(self):

        players = self.team.get_players()

        if not players:
            return []

        return sorted(
            players,
            key=lambda player: player.get_runs(),
            reverse=True
        )[:3]

    # -----------------------------------
    # Team Summary
    # -----------------------------------
    def get_team_summary(self):

        highest = self.get_highest_scorer()
        lowest = self.get_lowest_scorer()

        return {

            "Players":
                len(self.team.get_players()),

            "Total Runs":
                self.get_total_runs(),

            "Total Balls":
                self.get_total_balls(),

            "Average Runs":
                self.get_average_runs(),

            "Average Strike Rate":
                self.get_average_strike_rate(),

            "Highest Scorer":
                highest.get_name() if highest else "N/A",

            "Lowest Scorer":
                lowest.get_name() if lowest else "N/A"
        }