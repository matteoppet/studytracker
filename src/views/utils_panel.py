import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

from helpers import get_sum_in_time_format

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.window_id = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(self.window_id, width=e.width)) 
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.bind_mousewheel(canvas)

    def bind_mousewheel(self, widget):
        # windows/macos
        widget.bind_all("<MouseWheel>", lambda e: widget.yview_scroll(int(-1*(e.delta/120)), "units"))
        # linux
        widget.bind_all("<Button-4>", lambda e: widget.yview_scroll(-1, "units"))
        widget.bind_all("<Button-5>", lambda e: widget.yview_scroll(1, "units"))

class UtilsPanel(tk.Frame):
    def __init__(self, main_view):
        super().__init__(main_view)
        self.main_view = main_view

        self.profile_history_frame = tk.Frame(self, borderwidth=1, relief="solid")
        self.profile_history_frame.pack(side="top", fill="x", pady=(0,10))
        self.draw_profile_history_frame()

        self.routines_frame = tk.Frame(self)
        self.routines_frame.pack(side="top", fill="both", expand=True, pady=(10,0))
        self.draw_routines_frame()

    def draw_profile_history_frame(self):
        frame_profile = tk.Frame(self.profile_history_frame)
        frame_profile.pack(side="top", fill="x")
        
        self.profile_img_original = Image.open("assets/photos/test_profile_picture.jpg")
        self.profile_img_resized = self.profile_img_original.resize((50, 50), Image.Resampling.LANCZOS)
        self.profile_img_new = ImageTk.PhotoImage(self.profile_img_resized)
        self.profile_img_label = tk.Label(frame_profile, image=self.profile_img_new)
        self.profile_img_label.pack(side="left")
        tk.Label(frame_profile, text="BreaddPPitt").pack(side="left", padx=10)

        ttk.Separator(self.profile_history_frame, orient="horizontal").pack(fill="x")

        frame_history_and_friend = tk.Frame(self.profile_history_frame)
        frame_history_and_friend.pack(side="top", fill="both", pady=10, padx=10)

        notebook = ttk.Notebook(frame_history_and_friend)
        frame_history = tk.Frame(notebook)
        frame_friends = tk.Frame(notebook)
        notebook.add(frame_history, text="History")
        notebook.add(frame_friends, text="Friends")
        notebook.pack(expand=True, fill="both")

        self.draw_history_frame(frame_history)
        self.draw_friends_frame(frame_friends)

    def draw_routines_frame(self):
        title_frame = tk.Frame(self.routines_frame)
        title_frame.pack(side="top", fill="x", pady=10)
        tk.Label(title_frame, text="Routines", anchor="w", font=("TkDefaultFont", 25)).pack(side="left")
        tk.Button(title_frame, text="Create new", relief="groove").pack(side="right")
        ttk.Separator(self.routines_frame, orient="horizontal").pack(fill="x")

        tk.Button(self.routines_frame, text="Create temporary routine", relief="groove").pack(side="top", fill="x", pady=10)

        ttk.Separator(self.routines_frame, orient="horizontal").pack(fill="x")
        
        test_routines = {
            "Monday": {
                "Math": {"description": "Exercises", "time": "00:45"},
                "Chemistry": {"description": "Exercises", "time": "01:30"}
            },
            "Tuesday": {
                "Math": {"description": "Exercises", "time": "01:00"},
            },
            "Wednesday": {
                "Math": {"description": "Exercises", "time": "00:45"},
                "Chemistry": {"description": "Exercises", "time": "01:30"}
            },
            "Routine 4": {
                "Math": {"description": "Exercises", "time": "01:00"},
            }
        }

        scrollable_frame = ScrollableFrame(self.routines_frame)
        scrollable_frame.pack(side="top", fill="both", expand=True, pady=(10,0))

        self.arrow_icon = Image.open("assets/icons/arrow_icon.png")
        self.arrow_icon_resized = self.arrow_icon.resize((18, 18), Image.Resampling.LANCZOS)
        self.arrow_icon_new = ImageTk.PhotoImage(self.arrow_icon_resized)

        for routine, routine_info in test_routines.items():
            frame = tk.Frame(scrollable_frame.scrollable_frame, borderwidth=1, relief="solid")
            frame.pack(side="top", fill="x", pady=(10,0), expand=True, ipady=5)
            
            frame_title_routine = tk.Frame(frame)
            frame_title_routine.pack(side="top", fill="x")

            total_time_routine = get_sum_in_time_format([x["time"] for x in routine_info.values()])
            tk.Label(frame_title_routine, text=f"{str(routine)}: {total_time_routine[0]:02d}:{total_time_routine[1]:02d}", anchor="w", font=("TkDefaultFont", 10, "bold")).pack(side="left", fill="x", padx=5, pady=5)
            tk.Button(frame_title_routine, text="Select", relief="groove").pack(side="right", padx=5, pady=5)

            for subject, subject_info in routine_info.items():
                frame_subject = tk.Frame(frame)
                frame_subject.pack(side="top", fill="x", padx=5)

                tk.Label(frame_subject, image=self.arrow_icon_new).pack(side="left")
                tk.Label(frame_subject, text=subject).pack(side="left")

                tk.Label(frame_subject, text=subject_info["time"]).pack(side="right")      

                tk.Label(frame, text=subject_info["description"], foreground="gray", anchor="w").pack(side="top", fill="x", padx=(30,0))

    def draw_history_frame(self, frame):
        tk.Label(frame, text="History").pack()

    def draw_friends_frame(self, frame):
        tk.Label(frame, text="Friends").pack()


# TODO: put a calendar to plan each day on the routine page