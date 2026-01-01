import tkinter as tk
from tkinter import ttk

class TimerPanel(tk.Frame):
    def __init__(self, main_view):
        super().__init__(main_view, borderwidth=1, relief="solid")
        self.main_view = main_view

        self.timer_text = tk.StringVar(value="45:00")
        self.timer_text_font = 60

        self.daily_target_text = tk.StringVar(value="Daily Target: 1h 00m")

        self.draw()
    
    def draw(self):
        self.timer_label = tk.Label(self, textvariable=self.timer_text, font=("TkDefaultFont", self.timer_text_font))
        self.timer_label.pack(anchor="center", pady=40)

        self.button_start_stop = tk.Button(self, text="Start", relief="groove")
        self.button_start_stop.pack(fill="x", padx=10)
        self.button_pause = tk.Button(self, text="Pause", relief="groove", state="disabled")
        self.button_pause.pack(fill="x", padx=10, pady=5)

        ttk.Separator(self, orient='horizontal').pack(side="top", fill="x", pady=(10,15))

        self.button_customize = tk.Button(self, text="Customize", relief="groove")
        self.button_customize.pack(fill="x", padx=10)

        ttk.Separator(self, orient='horizontal').pack(side="top", fill="x", pady=(15,15))

        # TODO: show routine selected
        tk.Label(self, text="No routine selected").pack()

        daily_target_frame = tk.Frame(self)
        daily_target_frame.pack(side="bottom", pady=10, padx=10, fill="x")
        self.daily_target_label = tk.Label(daily_target_frame, textvariable=self.daily_target_text)
        self.daily_target_label.pack(side="left", fill="x")
        self.button_daily_target = tk.Button(daily_target_frame, text="Edit")
        self.button_daily_target.pack(side="right")

        ttk.Separator(self, orient='horizontal').pack(side="bottom", fill="x", pady=(10,0))