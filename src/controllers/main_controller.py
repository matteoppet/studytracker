import tkinter as tk
import views.main_view as main_view

class MainController:
    def __init__(self):
        self.main_view = main_view.MainView()

    def run(self):
        self.main_view.mainloop()