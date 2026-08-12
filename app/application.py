from models.batsman import Batsman
from models.team import Team

from services.parser import ScorecardParser
from services.analytics import Analytics
from services.charts import ChartService
from services.report import ReportService
from services.validator import Validator
from services.command_manager import CommandManager
from commands.add_player_command import AddPlayerCommand
from commands.update_player_command import UpdatePlayerCommand

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

        self.command_manager = CommandManager()
        

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

        if self.__team.search_player(name) is not None:
            return False, "Player already exists."


        player = Batsman(
            name,
            runs,
            balls
        )

        command = AddPlayerCommand(
            self.__team,
            player
        )

        try:

            self.command_manager.execute(command)

            return True, "Player added successfully."

        except Exception as e:

            return False, str(e)
        
     
    def update_player(
        self,
        old_name,
        new_name,
        runs,
        balls
    ):

        # ---------------------------------
        # Validate new data
        # ---------------------------------

        valid, message = Validator.validate_player(
            new_name,
            runs,
            balls
        )

        if not valid:
            return False, message

        # ---------------------------------
        # Find existing player
        # ---------------------------------

        player = self.__team.search_player(
            old_name
        )

        if player is None:
            return False, "Player not found."

        # ---------------------------------
        # Store old state
        # ---------------------------------

        old_runs = player.get_runs()
        old_balls = player.get_balls()

        # ---------------------------------
        # Check duplicate name
        # ---------------------------------

        if (
            old_name.lower() != new_name.lower()
            and self.__team.search_player(new_name)
            is not None
        ):

            return False, "Player already exists."

        # ---------------------------------
        # Create command
        # ---------------------------------

        command = UpdatePlayerCommand(
            player,
            old_name,
            old_runs,
            old_balls,
            new_name,
            runs,
            balls
        )

        # ---------------------------------
        # Execute command
        # ---------------------------------

        try:

            self.command_manager.execute(
                command
            )

            return True, "Player updated successfully."

        except Exception as e:

            return False, str(e)
            
        
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

        return self.__charts.generate_all_charts()

    # =====================================================
    # PDF
    # =====================================================

    def generate_pdf(self, filename=None):

        return self.__report.generate_pdf(filename)

    # =====================================================
    # Analytics
    # =====================================================

    def get_analytics(self):

        return self.__analytics


    # --------------------------------
    # Add Player
    # --------------------------------

    # def add_player(self, player):

    #     command = AddPlayerCommand(
    #         self.team,
    #         player
    #     )

    #     self.command_manager.execute(command)

    # --------------------------------
    # Undo
    # --------------------------------

    def undo(self):

        return self.command_manager.undo()

    # --------------------------------
    # Redo
    # --------------------------------

    def redo(self):

        return self.command_manager.redo()