import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib import styles
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image
)


class ReportService:

    REPORT_FOLDER = "reports"

    def __init__(self, team, analytics):

        self.__team = team
        self.__analytics = analytics

        os.makedirs(
            self.REPORT_FOLDER,
            exist_ok=True
        )

    # -------------------------------------
    # Generate PDF Report
    # -------------------------------------
    def generate_pdf(self, filename=None):

        if len(self.__team) == 0:
            raise ValueError(
                "No player data available."
            )

        if filename is None:

            filename = os.path.join(

                self.REPORT_FOLDER,

                f"Team_Report_{datetime.now():%Y%m%d_%H%M%S}.pdf"

            )

        pdf = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        elements = []

        # -------------------------
        # Title
        # -------------------------

        elements.append(
            Paragraph(
                "<b>Cricket Team Management System</b>",
                styles["Title"]
            )
        )

        elements.append(
            Paragraph(
                datetime.now().strftime("%d %B %Y"),
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # -------------------------
        # Player Table
        # -------------------------

        data = [
            [
                "Player",
                "Runs",
                "Balls",
                "Strike Rate"
            ]
        ]

        for player in self.__team:

            data.append([
                player.get_name(),
                player.get_runs(),
                player.get_balls(),
                f"{player.strike_rate():.2f}"
            ])

        table = Table(data)

        table.setStyle(

            TableStyle([

                ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

                ("TEXTCOLOR", (0,0), (-1,0), colors.white),

                ("GRID", (0,0), (-1,-1), 1, colors.black),

                ("BACKGROUND", (0,1), (-1,-1), colors.beige),

                ("ALIGN", (1,1), (-1,-1), "CENTER"),

                ("BOTTOMPADDING", (0,0), (-1,0), 8)

            ])

        )

        elements.append(table)

        elements.append(
            Spacer(1,20)
        )

        # -------------------------
        # Statistics
        # -------------------------

        report = self.__analytics.generate_report()


        highest = (
            report.highest_scorer.get_name()
            if report.highest_scorer
            else "N/A"
        )

        elements.append(
            Paragraph(
                "<b>Team Statistics</b>",
                styles["Heading2"]
            )
        )

        statistics = [

            f"Total Players : {report.total_players}",

            f"Total Runs : {report.total_runs}",

            f"Average Runs : {report.average_runs}",

            f"Average Strike Rate : {report.average_strike_rate}",

            f"Highest Scorer : {highest}"

        ]

        for item in statistics:

            elements.append(
                Paragraph(
                    item,
                    styles["Normal"]
                )
            )

        elements.append(
            Spacer(1,20)
        )

        # -------------------------
        # Charts
        # -------------------------

        charts = [

            "charts/runs_chart.png",

            "charts/strike_rate_chart.png",

            "charts/team_contribution.png"

        ]

        for chart in charts:

            if os.path.exists(chart):

                elements.append(
                    Image(chart, width=400, height=250)
                )

                elements.append(
                    Spacer(1,20)
                )     

        pdf.build(elements)

        return filename

       