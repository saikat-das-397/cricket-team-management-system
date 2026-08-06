import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ChartsWindow:

    def __init__(self, parent, app):

        self.app = app

        self.app.generate_charts()

        self.window = tk.Toplevel(parent)

        self.window.title("📊 Team Charts")

        self.window.geometry("900x650")

        self.window.transient(parent)

        self.window.grab_set()

        self.create_widgets()


    def create_widgets(self):

        top = ttk.Frame(self.window)

        top.pack(fill="x", pady=10)

        self.image_frame = ttk.Frame(self.window)

        self.image_frame.pack(
            fill="both",
            expand=True
        )

        ttk.Button(
            top,
            text="Runs",
            command=lambda: self.show_chart(
                "charts/runs_chart.png"
            )
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Strike Rate",
            command=lambda: self.show_chart(
                "charts/strike_rate_chart.png"
            )
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Contribution",
            command=lambda: self.show_chart(
                "charts/team_contribution.png"
            )
        ).pack(side="left", padx=5)

    def show_chart(self, filename):

        for widget in self.image_frame.winfo_children():
            widget.destroy()

        image = Image.open(filename)

        image.thumbnail((800, 500))

        photo = ImageTk.PhotoImage(image)

        label = ttk.Label(
            self.image_frame,
            image=photo
        )

        label.image = photo

        label.pack(expand=True)

    