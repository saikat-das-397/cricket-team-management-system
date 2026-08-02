class Team:

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    # --------------------------
    # Add Player
    # --------------------------
    def add_player(self, player):

        # Prevent duplicate names
        if self.search_player(player.get_name()) is not None:
            return False

        self.players.append(player)
        return True

    # --------------------------
    # Get Players
    # --------------------------
    def get_players(self):
        return self.players

    # --------------------------
    # Search Player
    # --------------------------
    def search_player(self, name):

        for player in self.players:

            if player.get_name().lower() == name.lower():
                return player

        return None

    # --------------------------
    # Update Player
    # --------------------------
    def update_player(self, name, runs, balls):

        player = self.search_player(name)

        if player is None:
            return False

        player.set_runs(runs)
        player.set_balls(balls)

        return True

    # --------------------------
    # Delete Player
    # --------------------------
    def delete_player(self, name):

        player = self.search_player(name)

        if player is None:
            return False

        self.players.remove(player)

        return True

    # --------------------------
    # Display Scorecard
    # --------------------------
    def display_scorecard(self):

        if len(self.players) == 0:

            print("\nNo players available.\n")
            return

        print("\n" + "=" * 65)
        print(f"Team : {self.team_name}")
        print("=" * 65)

        print(f"{'Player':<25}{'Runs':<10}{'Balls':<10}Strike Rate")
        print("-" * 65)

        for player in self.players:
            player.display()

        print("=" * 65)

    # --------------------------
    # Highest Scorer
    # --------------------------
    def highest_scorer(self):

        if len(self.players) == 0:
            return None

        return max(self.players, key=lambda player: player.get_runs())

    # --------------------------
    # Sort Players
    # --------------------------
    def sort_players(self):

        self.players.sort(
            key=lambda player: player.get_runs(),
            reverse=True
        )

    # --------------------------
    # Team Statistics
    # --------------------------
    def team_statistics(self):

        if len(self.players) == 0:
            return None

        total_runs = sum(player.get_runs() for player in self.players)

        total_balls = sum(player.get_balls() for player in self.players)

        average_sr = (
            sum(player.strike_rate() for player in self.players)
            / len(self.players)
        )

        highest = self.highest_scorer()

        return {
            "Players": len(self.players),
            "Total Runs": total_runs,
            "Total Balls": total_balls,
            "Average Strike Rate": round(average_sr, 2),
            "Highest Scorer": highest.get_name(),
            "Highest Runs": highest.get_runs()
        }


    def show_player(self, name):

        player = self.search_player(name)

        if player:

            print("\nPlayer Details")
            print("-" * 30)

            player.display_details()

            return True

        return False


    def show_highest_scorer(self):

        player = self.highest_scorer()

        if player:

            print("\nHighest Scorer")
            print("-" * 30)

            player.display_details()

            return True

        return False