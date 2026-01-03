import tkinter as tk
from tkinter import ttk

from .timer_panel import TimerPanel
from .utils_panel import UtilsPanel

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Tracker")
        self.geometry("1000x600")
        self.minsize(width=340, height=200)
        
        self.paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL, sashrelief="solid")

        self.timer_panel = TimerPanel(self)
        self.paned_window.add(self.timer_panel, padx=20, pady=20, minsize=300)

        self.utils_panel = UtilsPanel(self)
        self.paned_window.add(self.utils_panel, padx=20, pady=20, minsize=300)

        self.paned_window.pack(fill=tk.BOTH, expand=True)