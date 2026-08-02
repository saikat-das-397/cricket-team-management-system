import os
from datetime import datetime

from reportlab.lib import colors
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

    def __init__(self, team, analytics):

        self.team = team
        self.analytics = analytics

        os.makedirs("reports", exist_ok=True)

    # -------------------------------------
    # Generate PDF Report
    # -------------------------------------
    def generate_pdf(self):

        filename = (
            f"reports/Team_Report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
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

        for player in self.team.get_players():

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

        report = self.analytics.generate_report()

        elements.append(
            Paragraph("<b>Team Statistics</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                f"Total Players : {report.total_players}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Total Runs : {report.total_runs}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Average Runs : {report.average_runs}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Average Strike Rate : "
                f"{report.average_strike_rate}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Highest Scorer : "
                f"{report.highest_scorer.get_name()}",
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

        print(f"\nPDF created successfully!\n{filename}")