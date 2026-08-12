import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image,
    PageBreak
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

    # ==========================================
    # Generate PDF
    # ==========================================

    def generate_pdf(self, filename=None):

        players = self.__team.get_players()

        if not players:
            raise ValueError(
                "No player data available."
            )

        # --------------------------------------
        # Filename
        # --------------------------------------

        if filename is None:

            filename = os.path.join(
                self.REPORT_FOLDER,
                f"Team_Report_"
                f"{datetime.now():%Y%m%d_%H%M%S}.pdf"
            )

        # --------------------------------------
        # PDF Document
        # --------------------------------------

        pdf = SimpleDocTemplate(
            filename,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            fontSize=22,
            spaceAfter=10
        )

        subtitle_style = ParagraphStyle(
            "Subtitle",
            parent=styles["Normal"],
            alignment=TA_CENTER,
            fontSize=12,
            spaceAfter=5
        )

        section_style = ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontSize=15,
            spaceBefore=10,
            spaceAfter=10
        )

        elements = []

        # ======================================
        # HEADER
        # ======================================

        elements.append(
            Paragraph(
                "🏏 Cricket Team Management System",
                title_style
            )
        )

        elements.append(
            Paragraph(
                f"Team: {self.__team.get_team_name()}",
                subtitle_style
            )
        )

        elements.append(
            Paragraph(
                datetime.now().strftime(
                    "Generated: %d %B %Y at %I:%M %p"
                ),
                subtitle_style
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # ======================================
        # TEAM SUMMARY
        # ======================================

        elements.append(
            Paragraph(
                "Team Summary",
                section_style
            )
        )

        report = self.__analytics.generate_report()

        summary_data = [

            ["Metric", "Value"],

            [
                "Total Players",
                report.total_players
            ],

            [
                "Total Runs",
                report.total_runs
            ],

            [
                "Total Balls",
                report.total_balls
            ],

            [
                "Average Runs",
                report.average_runs
            ],

            [
                "Average Strike Rate",
                report.average_strike_rate
            ]

        ]

        summary_table = Table(
            summary_data,
            colWidths=[250, 150]
        )

        summary_table.setStyle(
            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.darkblue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.whitesmoke
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    8
                )

            ])
        )

        elements.append(summary_table)

        elements.append(
            Spacer(1, 20)
        )

        # ======================================
        # TOP PERFORMERS
        # ======================================

        elements.append(
            Paragraph(
                "Top Performers",
                section_style
            )
        )

        highest = self.__analytics.get_highest_scorer()

        best_sr = (
            self.__analytics
            .get_best_strike_rate_player()
        )

        performer_data = [

            ["Category", "Player", "Performance"],

            [
                "Highest Scorer",
                highest.get_name()
                if highest else "N/A",
                highest.get_runs()
                if highest else "N/A"
            ],

            [
                "Best Strike Rate",
                best_sr.get_name()
                if best_sr else "N/A",
                f"{best_sr.strike_rate():.2f}"
                if best_sr else "N/A"
            ]

        ]

        performer_table = Table(
            performer_data,
            colWidths=[150, 150, 100]
        )

        performer_table.setStyle(
            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.darkblue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "ALIGN",
                    (2, 1),
                    (2, -1),
                    "CENTER"
                )

            ])
        )

        elements.append(performer_table)

        elements.append(
            Spacer(1, 20)
        )

        # ======================================
        # TOP THREE
        # ======================================

        elements.append(
            Paragraph(
                "Top 3 Players",
                section_style
            )
        )

        top_three = (
            self.__analytics
            .get_top_three_players()
        )

        top_three_data = [
            ["Rank", "Player", "Runs", "Strike Rate"]
        ]

        for index, player in enumerate(
            top_three,
            start=1
        ):

            top_three_data.append([
                index,
                player.get_name(),
                player.get_runs(),
                f"{player.strike_rate():.2f}"
            ])

        top_three_table = Table(
            top_three_data,
            colWidths=[60, 180, 80, 100]
        )

        top_three_table.setStyle(
            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.darkblue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "ALIGN",
                    (0, 1),
                    (0, -1),
                    "CENTER"
                ),

                (
                    "ALIGN",
                    (2, 1),
                    (-1, -1),
                    "CENTER"
                )

            ])
        )

        elements.append(top_three_table)

        elements.append(
            PageBreak()
        )

        # ======================================
        # PLAYER SCORECARD
        # ======================================

        elements.append(
            Paragraph(
                "Player Scorecard",
                section_style
            )
        )

        player_data = [

            [
                "Player",
                "Runs",
                "Balls",
                "Strike Rate"
            ]

        ]

        for player in players:

            player_data.append([

                player.get_name(),

                player.get_runs(),

                player.get_balls(),

                f"{player.strike_rate():.2f}"

            ])

        player_table = Table(
            player_data,
            colWidths=[220, 80, 80, 100],
            repeatRows=1
        )

        player_table.setStyle(
            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.darkblue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.whitesmoke,
                        colors.lightgrey
                    ]
                )

            ])
        )

        elements.append(player_table)

        elements.append(
            Spacer(1, 25)
        )

        # ======================================
        # CHARTS
        # ======================================

        elements.append(
            Paragraph(
                "Performance Charts",
                section_style
            )
        )

        charts = [

            (
                "Runs Scored",
                "charts/runs_chart.png"
            ),

            (
                "Strike Rate Comparison",
                "charts/strike_rate_chart.png"
            ),

            (
                "Team Run Contribution",
                "charts/team_contribution.png"
            )

        ]

        for title, chart_path in charts:

            if os.path.exists(chart_path):

                elements.append(
                    Paragraph(
                        title,
                        styles["Heading3"]
                    )
                )

                elements.append(
                    Image(
                        chart_path,
                        width=6.2 * inch,
                        height=3.1 * inch
                    )
                )

                elements.append(
                    Spacer(1, 15)
                )

        # ======================================
        # FOOTER
        # ======================================

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                "Generated automatically by "
                "Cricket Team Management System v1.0",
                subtitle_style
            )
        )

        # ======================================
        # BUILD
        # ======================================

        pdf.build(elements)

        print(
            f"\nPDF created successfully!\n{filename}"
        )

        return filename