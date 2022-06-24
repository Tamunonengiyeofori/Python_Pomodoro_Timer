import tkinter as tk
from tkinter import ttk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



class GUI(tk.TK , Timer):
    
    def __init__(self):
        super().__init__()
        # ---------------------------- UI SETUP ------------------------------- #
        self.title("Pomodoro")
        self.config(padx=100 , pady=50 , bg=YELLOW)
        
        def create_gui(self):
            self.timer_label = ttk.Label(text="Timer")
            self.timer_label.config(fg=GREEN , bg=YELLOW , font=(FONT_NAME , 25 , "bold"))
            self.timer_label.grid(column=1 , row=0)

            # Create a canvas widget
            ## Canvas widget is used for 2D animations and drawings on the tkinter window
            self.canvas = ttk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 

            # Create an instance of a Photoimage class
            ## This class is used to read image files
            self.tomato_img = ttk.PhotoImage(file="tomato.png")
            self.canvas.create_image(100 , 112 , image=self.tomato_img)

            # Assign a variable to canvas.create_text to effect the countdown mechanism
            self.timer_text = self.canvas.create_text(100 , 130  , text="00:00" , fill="white" , font=(FONT_NAME, 35 , "bold "))  
            self.canvas.grid(column=1 ,row=1)

            # Call the countdown function when start buttton is clicked to effect the countdown mechanism
            self.start_button = ttk.Button(text="Start" , highlightthickness=0 , command=start_timer)
            self.start_button.grid(column=0, row=2)

            reset_button = Button(text="Reset" , highlightthickness=0 , command=reset_timer)
            reset_button.grid(column=2 ,row=2)

        # Create a checkbutton
        # def checkbutton_used():
        #     # Prints 1 if on button checked, otherwise 0 by default
        #     print(checked_state.get())

        # checked_state = IntVar()
        # check_button = Checkbutton(variable=checked_state , command=checkbutton_used)
        # check_button.grid(column=1 , row=3)

        checkmark_label = Label(bg=YELLOW)
        checkmark_label.grid(column=1 , row=3)

        window.mainloop()
        
            