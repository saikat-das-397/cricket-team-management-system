import tkinter as tk
from tkinter import ttk


class StatisticsWindow:

    def __init__(self, parent, app):

        self.app = app

        self.window = tk.Toplevel(parent)

        self.window.title("📊 Team Statistics")

        self.window.geometry("500x600")

        self.window.resizable(False, False)

        self.window.transient(parent)
        self.window.grab_set()

        self.create_widgets()

    # ----------------------------------------
    # Create Widgets
    # ----------------------------------------

    def create_widgets(self):

        report = self.app.get_analytics().generate_report()

        frame = ttk.Frame(
            self.window,
            padding=20
        )

        frame.pack(fill="both", expand=True)

        # -------------------------
        # Title
        # -------------------------

        ttk.Label(
            frame,
            text="📊 Team Statistics",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(0, 20))

        # -------------------------
        # Statistics
        # -------------------------

        highest = (
            f"{report.highest_scorer.get_name()} "
            f"({report.highest_scorer.get_runs()} Runs)"
            if report.highest_scorer else "N/A"
        )

        lowest = (
            f"{report.lowest_scorer.get_name()} "
            f"({report.lowest_scorer.get_runs()} Runs)"
            if report.lowest_scorer else "N/A"
        )

        stats = [

            ("Players", report.total_players),

            ("Total Runs", report.total_runs),

            ("Total Balls", report.total_balls),

            ("Average Runs", report.average_runs),

            ("Average Strike Rate", report.average_strike_rate),

            ("Highest Scorer", highest),

            ("Lowest Scorer", lowest)

        ]

        for label, value in stats:

            row = ttk.Frame(frame)

            row.pack(fill="x", pady=5)

            ttk.Label(
                row,
                text=label,
                width=22,
                anchor="w",
                font=("Segoe UI", 11, "bold")
            ).pack(side="left")

            ttk.Label(
                row,
                text=str(value),
                font=("Segoe UI", 11)
            ).pack(side="left")

        # -------------------------
        # Separator
        # -------------------------

        ttk.Separator(frame).pack(
            fill="x",
            pady=15
        )

        # -------------------------
        # Top 3 Players
        # -------------------------

        ttk.Label(
            frame,
            text="🏆 Top 3 Players",
            font=("Segoe UI", 14, "bold")
        ).pack()

        top_players = self.app.get_analytics().get_top_three_players()

        if not top_players:

            ttk.Label(
                frame,
                text="No players available."
            ).pack(pady=10)

        else:

            for index, player in enumerate(top_players, start=1):

                ttk.Label(
                    frame,
                    text=f"{index}. {player.get_name()} ({player.get_runs()} Runs)",
                    font=("Segoe UI", 11)
                ).pack(anchor="w", padx=30, pady=2)

        # -------------------------
        # Close Button
        # -------------------------

        ttk.Button(
            frame,
            text="Close",
            command=self.window.destroy
        ).pack(pady=20)