import tkinter as tk
from tkinter import ttk

from app.application import Application
from tkinter import filedialog, messagebox
from gui.player_dialog import PlayerDialog


class MainWindow:

    def __init__(self):

        self.app = Application("Bangladesh")

        self.root = tk.Tk()

        self.root.title("🏏 Cricket Team Management System")

        self.root.geometry("1100x700")

        self.style = ttk.Style()
        self.style.theme_use("aqua")

        # THIS MUST EXIST
        self.create_widgets()
    # -----------------------------
    # Create Widgets
    # -----------------------------


    def create_widgets(self):

        # Create Menu
        self.create_menu()

        # ===========================
        # Top Frame
        # ===========================
        self.top_frame = ttk.Frame(self.root, padding=10)
        self.top_frame.pack(fill="x")

        title = ttk.Label(
            self.top_frame,
            text="🏏 Cricket Team Management System",
            font=("Segoe UI", 20, "bold")
        )

        title.pack()

        # ===========================
        # Information Frame
        # ===========================
        self.info_frame = ttk.Frame(self.root, padding=10)
        self.info_frame.pack(fill="x")

        self.team_label = ttk.Label(
            self.info_frame,
            text=f"Team : {self.app.get_team().get_team_name()}",
            font=("Segoe UI", 12)
        )

        self.team_label.pack(side="left")

        self.player_count = ttk.Label(
            self.info_frame,
            text="Players : 0",
            font=("Segoe UI", 12)
        )

        self.player_count.pack(side="right")

        # ===========================
        # Content Frame
        # ===========================

        self.content_frame = ttk.Frame(self.root)

        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ---------------------------
        # Player Table
        # ---------------------------

        columns = (
            "name",
            "runs",
            "balls",
            "strike_rate"
        )

        self.table = ttk.Treeview(

            self.content_frame,

            columns=columns,

            show="headings"

        )

        scrollbar = ttk.Scrollbar(

            self.content_frame,

            orient="vertical",

            command=self.table.yview

        )

        self.table.configure(

            yscrollcommand=scrollbar.set

        )

        scrollbar.pack(

            side="right",

            fill="y"

        )

        self.table.pack(

            fill="both",

            expand=True,

            side="left"

        )

        self.table.heading(
            "name",
            text="Player Name"
        )

        self.table.heading(
            "runs",
            text="Runs"
        )

        self.table.heading(
            "balls",
            text="Balls"
        )

        self.table.heading(
            "strike_rate",
            text="Strike Rate"
        )

        self.table.column(
            "name",
            width=250
        )

        self.table.column(
            "runs",
            width=100,
            anchor="center"
        )

        self.table.column(
            "balls",
            width=100,
            anchor="center"
        )

        self.table.column(
            "strike_rate",
            width=120,
            anchor="center"
        )

        self.table.pack(
            fill="both",
            expand=True
        )

        # ===========================
        # Status Bar
        # ===========================
        self.status = ttk.Label(
            self.root,
            text="Ready",
            anchor="w"
        )

        self.status.pack(
            side="bottom",
            fill="x"
        )

    def create_menu(self):

        menu_bar = tk.Menu(self.root)

        # =====================
        # File Menu
        # =====================

        file_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        file_menu.add_command(
            label="Load Scorecard",
            command=self.load_scorecard
        )

        file_menu.add_command(
            label="Save Scorecard",
            command=self.save_scorecard
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=self.root.quit
        )

        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )

        # =====================
        # Players Menu
        # =====================

        player_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        player_menu.add_command(label="Add Player", command=self.add_player)

        player_menu.add_command(label="Update Player", command=self.update_player)

        player_menu.add_command(label="Delete Player", command=self.delete_player)

        player_menu.add_command(label="Search Player", command=self.search_player)

        menu_bar.add_cascade(
            label="Players",
            menu=player_menu
        )

        # =====================
        # Analytics
        # =====================

        analytics_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        analytics_menu.add_command(
            label="Team Statistics"
        )

        analytics_menu.add_command(
            label="Highest Scorer"
        )

        analytics_menu.add_command(
            label="Generate Charts"
        )

        menu_bar.add_cascade(
            label="Analytics",
            menu=analytics_menu
        )

        # =====================
        # Reports
        # =====================

        report_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        report_menu.add_command(
            label="Generate PDF"
        )

        menu_bar.add_cascade(
            label="Reports",
            menu=report_menu
        )

        # =====================
        # Help
        # =====================

        help_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        help_menu.add_command(
            label="About"
        )

        menu_bar.add_cascade(
            label="Help",
            menu=help_menu
        )

        self.root.config(menu=menu_bar)



    def refresh_table(self):

        # Clear old rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert latest data
        players = self.app.get_players()

        for player in players:

            self.table.insert(

                "",

                "end",

                values=(

                    player.get_name(),

                    player.get_runs(),

                    player.get_balls(),

                    f"{player.strike_rate():.2f}"

                )

            )

        # Update player count
        self.player_count.config(
            text=f"Players : {len(players)}"
        )



    def load_scorecard(self):

        filename = filedialog.askopenfilename(

                title="Select Scorecard",

                filetypes=[
                    ("Text Files", "*.txt")
                ]

            )

        if not filename:
                return

        try:

            self.app.load(filename)

            self.refresh_table()

            self.status.config(
                    text="Scorecard loaded successfully."
           )

            messagebox.showinfo(
                "Success",
                "Scorecard loaded successfully!"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )



    def save_scorecard(self):

        filename = filedialog.asksaveasfilename(

            title="Save Scorecard",

            defaultextension=".txt",

            filetypes=[
                ("Text Files", "*.txt")
            ]
        )

        if not filename:
            return

        try:

            self.app.save(filename)

            self.status.config(
                text="Scorecard saved successfully."
            )

            messagebox.showinfo(
                "Success",
                "Scorecard saved successfully!"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def add_player(self):

        dialog = PlayerDialog(self.root)

        self.root.wait_window(dialog.window)

        if dialog.result is None:
            return

        name, runs, balls = dialog.result

        # --------------------------
        # Validation
        # --------------------------

        try:

            runs = int(runs)
            balls = int(balls)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Runs and Balls must be numbers."
            )

            return

        success, message = self.app.add_player(
            name,
            runs,
            balls
        )

        if success:

            self.refresh_table()

            messagebox.showinfo(
                "Success",
                message
            )

        else:

            messagebox.showerror(
                "Validation Error",
                message
            )

        if not success:

            messagebox.showerror(
                "Duplicate",
                "Player already exists."
            )

            return

        self.refresh_table()

        self.status.config(
            text=f"{name} added successfully."
        )

        messagebox.showinfo(
            "Success",
            "Player added successfully!"
        )


    def update_player(self):

        selected = self.table.selection()

        if not selected:

            messagebox.showwarning(
                "Update Player",
                "Please select a player."
            )

            return

        values = self.table.item(
            selected[0],
            "values"
        )

        old_name = values[0]

        player = self.app.search_player(old_name)


        dialog = PlayerDialog(
            self.root,
            title="Update Player",
            player=player
        )

        self.root.wait_window(dialog.window)

        if dialog.result is None:
            return

        new_name, runs, balls = dialog.result

        try:

            runs = int(runs)
            balls = int(balls)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Runs and Balls must be numbers."
            )

            return

        success, message = self.app.update_player(
            old_name,
            new_name,
            runs,
            balls
        )

        if success:

            self.refresh_table()

            self.status.config(
                text=message
            )

            messagebox.showinfo(
                "Success",
                message
            )

        else:

            messagebox.showerror(
                "Error",
                message
            )


    def delete_player(self):

        # Get selected row
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "Delete Player",
                "Please select a player."
            )
            return

        values = self.table.item(selected[0], "values")
        player_name = values[0]

        # Confirmation dialog
        answer = messagebox.askyesno(
            "Delete Player",
            f"Are you sure you want to delete\n\n{player_name}?"
        )

        if not answer:
            return

        success, message = self.app.delete_player(player_name)

        if success:

            self.refresh_table()

            self.status.config(text=message)

            messagebox.showinfo(
                "Success",
                message
            )

        else:

            messagebox.showerror(
                "Error",
                message
            )

    def search_player(self):
        pass
    # -----------------------------
    # Run
    # -----------------------------

    def run(self):

        self.root.mainloop()