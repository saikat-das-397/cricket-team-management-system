from models.batsman import Batsman
from models.team import Team

from services.parser import ScorecardParser
from services.analytics import Analytics
from services.charts import ChartService
from services.report import ReportService
from services.validator import Validator


class Application:
    """
    Main application controller.

    Coordinates all services.

    The GUI communicates ONLY with this class.
    """

    DEFAULT_FILE = "data/scorecard.txt"

    def __init__(self, team_name: str = "My Team"):

        # -------------------------
        # Core Model
        # -------------------------

        self.__team = Team(team_name)

        # -------------------------
        # Services
        # -------------------------

        self.__parser = ScorecardParser()

        self.__analytics = Analytics(self.__team)

        self.__charts = ChartService(self.__team)

        self.__report = ReportService(
            self.__team,
            self.__analytics
        )

    # =====================================================
    # File Operations
    # =====================================================

    def load(
        self,
        filename: str = DEFAULT_FILE
    ) -> bool:

        try:

            players = self.__parser.read_file(filename)

            self.__team.clear()

            for player in players:
                self.__team.add_player(player)

            return True

        except FileNotFoundError:
            return False

    def save(
        self,
        filename: str = DEFAULT_FILE
    ) -> bool:

        try:

            self.__parser.save_file(
                filename,
                self.__team.get_players()
            )

            return True

        except FileNotFoundError:
            return False

    # =====================================================
    # Player Operations
    # =====================================================

    def add_player(self, name, runs, balls):

        valid, message = Validator.validate_player(
            name,
            runs,
            balls
        )

        if not valid:
            return False, message


        player = Batsman(name, runs, balls)

        return self.__team.add_player(player)
    
    def update_player(
        self,
        old_name,
        new_name,
        runs,
        balls
    ):

        valid, message = Validator.validate_player(
            new_name,
            runs,
            balls
        )

        if not valid:
            return False, message

        success = self.__team.update_player(
            old_name,
            new_name,
            runs,
            balls
        )

        if not success:
            return False, "Player already exists."

        return True, "Player updated successfully."

    def delete_player(self, name):

        if self.__team.delete_player(name):
            return True, "Player deleted successfully."

        return False, "Player not found."

    def search_player(self, name):

        return self.__team.search_player(name)

    # =====================================================
    # Getters
    # =====================================================

    def get_players(self):

        return self.__team.get_players()

    def get_team(self):

        return self.__team

    def get_report(self):

        return self.__analytics.generate_report()

    def get_top_players(self):

        return self.__analytics.get_top_three_players()

    # =====================================================
    # Charts
    # =====================================================

    def generate_charts(self):

        self.__charts.generate_all_charts()

    # =====================================================
    # PDF
    # =====================================================

    def generate_pdf(self, filename=None):

        self.__report.generate_pdf(filename)

    # =====================================================
    # Analytics
    # =====================================================

    def get_analytics(self):

        return self.__analytics