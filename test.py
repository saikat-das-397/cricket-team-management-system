import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.configure(bg="white")

label = tk.Label(
    root,
    text="Tkinter Works!",
    font=("Arial", 24),
    bg="yellow",
    fg="black"
)

label.pack(expand=True)

root.mainloop()