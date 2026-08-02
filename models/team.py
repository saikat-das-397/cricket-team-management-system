from models.player import Player


class Team:
    """
    Represents a cricket team and manages its players.
    """

    def __init__(self, team_name: str):
        self.__team_name = team_name
        self.__players = []

    # ==========================================
    # Getters
    # ==========================================

    def get_team_name(self) -> str:
        return self.__team_name

    def get_players(self) -> list:
        return self.__players

    def player_count(self) -> int:
        return len(self.__players)

    # ==========================================
    # Player Management
    # ==========================================

    def add_player(self, player: Player) -> bool:
        """
        Add a player if the name is unique.
        """

        if self.search_player(player.get_name()):
            return False

        self.__players.append(player)
        return True

    def search_player(self, name: str) -> Player | None:
        """
        Search player by name.
        """

        for player in self.__players:

            if player.get_name().lower() == name.lower():
                return player

        return None

    def update_player(
        self,
        name: str,
        runs: int,
        balls: int
    ) -> bool:
        """
        Update player's runs and balls.
        """

        player = self.search_player(name)

        if player is None:
            return False

        player.set_runs(runs)
        player.set_balls(balls)

        return True

    def delete_player(self, name: str) -> bool:
        """
        Delete player by name.
        """

        player = self.search_player(name)

        if player is None:
            return False

        self.__players.remove(player)

        return True

    # ==========================================
    # Utility Methods
    # ==========================================

    def sort_by_runs(self, reverse=True) -> None:
        """
        Sort players by runs.
        """

        self.__players.sort(
            key=lambda player: player.get_runs(),
            reverse=reverse
        )

    def clear(self) -> None:
        """
        Remove all players.
        """

        self.__players.clear()

    def is_empty(self) -> bool:
        """
        Check whether the team has players.
        """

        return len(self.__players) == 0

    # ==========================================
    # Magic Methods
    # ==========================================

    def __len__(self):
        return len(self.__players)

    def __iter__(self):
        return iter(self.__players)

    def __str__(self):
        return (
            f"Team: {self.__team_name} "
            f"({len(self.__players)} players)"
        )