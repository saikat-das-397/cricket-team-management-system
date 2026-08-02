from abc import ABC, abstractmethod


class Player(ABC):
    """
    Abstract base class representing a cricket player.
    """

    STRIKE_RATE_MULTIPLIER = 100

    def __init__(self, name: str, runs: int, balls: int):
        self.set_name(name)
        self.set_runs(runs)
        self.set_balls(balls)

    # ==================================
    # Getters
    # ==================================

    def get_name(self) -> str:
        return self.__name

    def get_runs(self) -> int:
        return self.__runs

    def get_balls(self) -> int:
        return self.__balls

    # ==================================
    # Setters
    # ==================================

    def set_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Player name cannot be empty.")

        self.__name = name.strip()

    def set_runs(self, runs: int) -> None:
        if runs < 0:
            raise ValueError("Runs cannot be negative.")

        self.__runs = runs

    def set_balls(self, balls: int) -> None:
        if balls < 0:
            raise ValueError("Balls cannot be negative.")

        self.__balls = balls

    # ==================================
    # Common Methods
    # ==================================

    def strike_rate(self) -> float:
        """
        Calculate the strike rate.
        """

        if self.__balls == 0:
            return 0.0

        return (
            self.__runs / self.__balls
        ) * self.STRIKE_RATE_MULTIPLIER

    def to_list(self) -> list:
        """
        Return player data as a list.
        Useful for Treeview and tables.
        """

        return [
            self.__name,
            self.__runs,
            self.__balls,
            round(self.strike_rate(), 2)
        ]

    def to_dict(self) -> dict:
        """
        Return player data as a dictionary.
        Useful for JSON or reports.
        """

        return {
            "name": self.__name,
            "runs": self.__runs,
            "balls": self.__balls,
            "strike_rate": round(self.strike_rate(), 2)
        }

    # ==================================
    # Special Methods
    # ==================================

    def __str__(self) -> str:
        return (
            f"{self.__name} | "
            f"Runs: {self.__runs} | "
            f"Balls: {self.__balls}"
        )

    def __eq__(self, other) -> bool:

        if not isinstance(other, Player):
            return False

        return self.__name.lower() == other.get_name().lower()

    # ==================================
    # Abstract Methods
    # ==================================

    @abstractmethod
    def display(self):
        """
        Must be implemented by subclasses.
        """
        pass

    # ==================================
    # Display
    # ==================================

    def display_details(self) -> None:

        print("-" * 35)
        print(f"Name        : {self.__name}")
        print(f"Runs        : {self.__runs}")
        print(f"Balls       : {self.__balls}")
        print(f"Strike Rate : {self.strike_rate():.2f}")
        print("-" * 35)