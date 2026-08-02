from models.team import Team

from services.parser import ScorecardParser
from services.analytics import Analytics
from services.charts import ChartService
from services.report import ReportService


class Application:
    """
    Main Application Controller.

    This class connects all parts of the system.

    GUI never talks directly to Team,
    Parser, Analytics, Charts or Report.

    GUI only talks to Application.
    """

    def __init__(self, team_name="My Team"):

        # -------------------------
        # Core Model
        # -------------------------

        self.team = Team(team_name)

        # -------------------------
        # Services
        # -------------------------

        self.parser = ScorecardParser()

        self.analytics = Analytics(self.team)

        self.charts = ChartService(self.team)

        self.report = ReportService(
            self.team,
            self.analytics
        )

    # --------------------------------
    # Load Data
    # --------------------------------

    def load(self, filename="data/scorecard.txt"):

        self.parser.read_file(
            filename,
            self.team
        )

    # --------------------------------
    # Save Data
    # --------------------------------

    def save(self, filename="data/scorecard.txt"):

        self.parser.write_file(
            filename,
            self.team
        )

    # --------------------------------
    # Get Team
    # --------------------------------

    def get_team(self):

        return self.team

    # --------------------------------
    # Get Analytics
    # --------------------------------

    def get_analytics(self):

        return self.analytics

    # --------------------------------
    # Generate Charts
    # --------------------------------

    def generate_charts(self):

        self.charts.generate_all_charts()

    # --------------------------------
    # Generate PDF
    # --------------------------------

    def generate_pdf(self):

        self.report.generate_pdf()