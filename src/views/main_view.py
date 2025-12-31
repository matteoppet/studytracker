import tkinter as tk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Tracker")
        self.geometry("600x400")

        tk.Label(self, text="Welcome to Study Tracker!").pack(pady=20)