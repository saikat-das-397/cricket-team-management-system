class TeamReport:
    """
    Stores all team statistics.

    This class is a Data Transfer Object (DTO).

    It stores data but contains almost no business logic.
    """

    def __init__(
        self,
        total_players,
        total_runs,
        total_balls,
        average_runs,
        average_strike_rate,
        highest_scorer,
        lowest_scorer,
        top_three_players
    ):

        self.total_players = total_players
        self.total_runs = total_runs
        self.total_balls = total_balls

        self.average_runs = average_runs
        self.average_strike_rate = average_strike_rate

        self.highest_scorer = highest_scorer
        self.lowest_scorer = lowest_scorer

        self.top_three_players = top_three_players