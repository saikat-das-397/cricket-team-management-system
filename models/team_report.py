from dataclasses import dataclass
from models.player import Player

@dataclass
class TeamReport:
    total_players: int
    total_runs: int
    total_balls: int
    average_runs: float
    average_strike_rate: float
    highest_scorer: Player | None
    lowest_scorer: Player | None
    best_strike_rate_player: Player | None = None
