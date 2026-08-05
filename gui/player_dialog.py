import tkinter as tk
from tkinter import ttk


class PlayerDialog:

    def __init__(self, parent,title="Add Player", player=None):

        self.result = None

        self.window = tk.Toplevel(parent)

        self.window.title(title)

        self.window.geometry("420x400")

        self.window.resizable(False, False)

        self.window.transient(parent)   # Keep dialog on top of parent
        self.window.grab_set()          # Make it modal
        self.window.focus_set()         # Give it keyboard focus
        self.window.wait_visibility()   # Wait until visible

        # -----------------------
        # Name
        # -----------------------

        ttk.Label(
            self.window,
            text="Player Name"
        ).pack(pady=(15, 5))

        self.name_entry = ttk.Entry(
            self.window,
            width=35
        )

        self.name_entry.pack()

        # -----------------------
        # Runs
        # -----------------------

        ttk.Label(
            self.window,
            text="Runs"
        ).pack(pady=(10, 5))

        self.runs_entry = ttk.Entry(
            self.window,
            width=20
        )

        self.runs_entry.pack()

        # -----------------------
        # Balls
        # -----------------------

        ttk.Label(
            self.window,
            text="Balls"
        ).pack(pady=(10, 5))

        self.balls_entry = ttk.Entry(
            self.window,
            width=20
        )

        self.balls_entry.pack()

        # -----------------------
        # Buttons
        # -----------------------

        frame = ttk.Frame(self.window)
        frame.pack(pady=20)

        ttk.Button(
            frame,
            text="Save",
            command=self.save
        ).pack(side="left", padx=10)

        ttk.Button(
            frame,
            text="Cancel",
            command=self.window.destroy
        ).pack(side="left")

        if player is not None:

            self.name_entry.insert(
                0,
                player.get_name()
            )

            self.runs_entry.insert(
                0,
                str(player.get_runs())
            )

            self.balls_entry.insert(
                0,
                str(player.get_balls())
            )

    def save(self):

        self.result = (

            self.name_entry.get(),

            self.runs_entry.get(),

            self.balls_entry.get()

        )

        self.window.destroy()