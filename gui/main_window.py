import tkinter as tk
from tkinter import ttk

from app.application import Application
from tkinter import filedialog, messagebox
from gui.player_dialog import PlayerDialog
from gui.statistics_window import StatisticsWindow
from gui.charts_window import ChartsWindow

class MainWindow:

    def __init__(self):

        self.app = Application("Bangladesh")

        self.root = tk.Tk()

        self.root.title("🏏 Cricket Team Management System")

        self.root.geometry("1100x700")

        self.style = ttk.Style()
        self.style.theme_use("aqua")
        self.create_toolbar()
        # THIS MUST EXIST
        self.create_widgets()
        self.bind_shortcuts()
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

        # ===========================
        # Search Frame
        # ===========================

        self.search_frame = ttk.Frame(self.root, padding=10)
        self.search_frame.pack(fill="x")

        ttk.Label(
            self.search_frame,
            text="🔍 Search Player:"
        ).pack(side="left")

        self.search_var = tk.StringVar()

        search_entry = ttk.Entry(
            self.search_frame,
            textvariable=self.search_var,
            width=30
        )

        search_entry.pack(side="left", padx=10)

        # Whenever text changes
        self.search_var.trace_add(
            "write",
            self.search_players
        )

        self.table = ttk.Treeview(

            self.content_frame,

            columns=columns,

            show="headings"

        )

        self.context_menu = tk.Menu(
            self.root,
            tearoff=0
        )

        self.context_menu.add_command(
            label="✏ Update Player",
            command=self.update_player
        )

        self.context_menu.add_command(
            label="❌ Delete Player",
            command=self.delete_player
        )

        self.context_menu.add_separator()

        self.context_menu.add_command(
            label="👁 View Details",
            command=self.view_player
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

        self.table.bind(
            "<Double-1>",
            self.on_double_click
        )

        self.table.bind(
            "<Button-3>",
            self.show_context_menu
        )

        self.table.heading(
            "name",
            text="Player Name",
            command=lambda: self.sort_table("name", False)
        )

        self.table.heading(
            "runs",
            text="Runs",
            command=lambda: self.sort_table("runs", False)
        )

        self.table.heading(
            "balls",
            text="Balls",
            command=lambda: self.sort_table("balls", False)
        )

        self.table.heading(
            "strike_rate",
            text="Strike Rate",
            command=lambda: self.sort_table("strike_rate", False)
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
            label="Load Scorecard \tCtrl+O",
            command=self.load_scorecard
        )

        file_menu.add_command(
            label="Save Scorecard \tCtrl+S",
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

        player_menu.add_command(label="Add Player \tCtrl+N", command=self.add_player)

        player_menu.add_command(label="Update Player \tCtrl+U", command=self.update_player)

        player_menu.add_command(label="Delete Player \tCtrl+D", command=self.delete_player)

        player_menu.add_command(label="Search Player \tCtrl+F", command=self.search_players)

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
            label="Team Statistics",
            command=self.show_statistics
        )

        analytics_menu.add_command(
            label="Highest Scorer"
        )

        analytics_menu.add_command(
            label="Generate Charts",
            command=self.show_charts
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
            label="Generate PDF",
            command=self.generate_pdf
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

        self.populate_table(players)

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

        # messagebox.showinfo(
        #     "Success",
        #     "Player added successfully!"
        # )


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

    def search_players(self, *args):

        keyword = self.search_var.get().strip().lower()

        # Clear current table
        players = [
            player
            for player in self.app.get_players()
            if keyword in player.get_name().lower()
        ]

        self.populate_table(players)


    def populate_table(self, players):

        self.table.delete(*self.table.get_children())

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

    def show_statistics(self):

        StatisticsWindow(
            self.root,
            self.app
        )


    def show_charts(self):

        ChartsWindow(
            self.root,
            self.app
        )

    def sort_table(self, column, reverse):

        # Get all rows
        data = [
            (self.table.set(item, column), item)
            for item in self.table.get_children("")
        ]

        # Numeric columns
        if column in ("runs", "balls", "strike_rate"):

            data.sort(
                key=lambda x: float(x[0]),
                reverse=reverse
            )

        else:

            data.sort(
                key=lambda x: x[0].lower(),
                reverse=reverse
            )

        # Rearrange rows
        for index, (_, item) in enumerate(data):

            self.table.move(
                item,
                "",
                index
            )

        # Next click reverses order
        self.table.heading(
            column,
            command=lambda: self.sort_table(
                column,
                not reverse
            )
        )

    def on_double_click(self, event):

        item = self.table.identify_row(event.y)

        if not item:
            return

        self.table.selection_set(item)

        self.update_player()


    def show_context_menu(self, event):

        item = self.table.identify_row(event.y)

        if not item:
            return

        self.table.selection_set(item)

        self.context_menu.post(
            event.x_root,
            event.y_root
        )


    def view_player(self):

        selected = self.table.selection()

        if not selected:
            return

        values = self.table.item(
            selected[0],
            "values"
        )

        messagebox.showinfo(

            "Player Details",

            f"Name : {values[0]}\n"
            f"Runs : {values[1]}\n"
            f"Balls : {values[2]}\n"
            f"Strike Rate : {values[3]}"
        )

    # -----------------------------
    # Keyboard Shortcuts
    # -----------------------------
    def bind_shortcuts(self):

        self.root.bind(
            "<Control-n>",
            lambda event: self.add_player()
        )

        self.root.bind(
            "<Control-o>",
            lambda event: self.load_scorecard()
        )

        self.root.bind(
            "<Control-s>",
            lambda event: self.save_scorecard()
        )

        self.root.bind(
            "<Control-p>",
            lambda event: self.generate_pdf()
        )

        self.root.bind(
            "<Control-u>",
            lambda event: self.update_player()
        )

        self.root.bind(
            "<Control-d>",
            lambda event: self.delete_player()
        )

        self.root.bind(
            "<Control-z>",
            lambda event: self.undo()
        )

        self.root.bind(
            "<Control-y>",
            lambda event: self.redo()
        )


    def generate_pdf(self):

        filename = filedialog.asksaveasfilename(
            title="Save PDF Report",
            defaultextension=".pdf",
            filetypes=[
                ("PDF Files", "*.pdf")
            ]
        )

        if not filename:
            return

        try:

            generated_file = self.app.generate_pdf(filename)

            self.status.config(
                text="PDF report generated successfully."
            )

            messagebox.showinfo(
                "Success",
                f"PDF report generated successfully!\n\n"
                f"Saved to:\n{generated_file}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )
    # -----------------------------
    # Run
    # -----------------------------

    def create_toolbar(self):

        self.toolbar = ttk.Frame(
            self.root,
            padding=5
        )

        self.toolbar.pack(
            fill="x",
            side="top"
        )

        # -------------------------
        # Load
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="📂 Load",
            command=self.load_scorecard
        ).pack(
            side="left",
            padx=3
        )

        # -------------------------
        # Save
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="💾 Save",
            command=self.save_scorecard
        ).pack(
            side="left",
            padx=3
        )

        # -------------------------
        # Add
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="➕ Add",
            command=self.add_player
        ).pack(
            side="left",
            padx=3
        )

        # -------------------------
        # Update
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="✏ Update",
            command=self.update_player
        ).pack(
            side="left",
            padx=3
        )

        # -------------------------
        # Delete
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="❌ Delete",
            command=self.delete_player
        ).pack(
            side="left",
            padx=3
        )

        # Separator
        ttk.Separator(
            self.toolbar,
            orient="vertical"
        ).pack(
            side="left",
            fill="y",
            padx=8
        )

        # -------------------------
        # Statistics
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="📊 Statistics",
            command=self.show_statistics
        ).pack(
            side="left",
            padx=3
        )

        # -------------------------
        # Charts
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="📈 Charts",
            command=self.show_charts
        ).pack(
            side="left",
            padx=3
        )

        # -------------------------
        # PDF
        # -------------------------

        ttk.Button(
            self.toolbar,
            text="📄 PDF",
            command=self.generate_pdf
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            self.toolbar,
            text="↶ Undo",
            command=self.undo
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            self.toolbar,
            text="↷ Redo",
            command=self.redo
        ).pack(
            side="left",
            padx=3
        )


    def undo(self):

        if self.app.undo():

            self.populate_table(
                self.app.get_players()
            )

            self.status.config(
                text="Last action undone."
            )

        else:

            self.status.config(
                text="Nothing to undo."
            )

    def redo(self):

        if self.app.redo():

            self.populate_table(
                self.app.get_players()
            )

            self.status.config(
                text="Last action redone."
            )

        else:

            self.status.config(
                text="Nothing to redo."
            )      

        
    def run(self):

        self.root.mainloop()