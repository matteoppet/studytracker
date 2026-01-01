import tkinter as tk
from tkinter import ttk

class UtilsPanel(tk.Frame):
    def __init__(self, main_view):
        super().__init__(main_view)
        self.main_view = main_view

        self.history_frame = tk.Frame(self, borderwidth=1, relief="solid")
        self.history_frame.pack(side="top", fill="x", pady=(0,10))
        self.draw_history_frame()

        self.routines_frame = tk.Frame(self, borderwidth=1, relief="solid")
        self.routines_frame.pack(side="top", fill="both", expand=True, pady=(10,0))
        self.draw_routines_frame()

    def draw_history_frame(self):
        tk.Label(self.history_frame, text="History Frame...").pack()

    def draw_routines_frame(self):
        tk.Label(self.routines_frame, text="Routines Frame...").pack()