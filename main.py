from tkinter import*
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0 
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    if REPS >= 1:
        REPS -= 1
    window.after_cancel(TIMER)
    timer_label.config(text="Timer" , fg=GREEN)
    canvas.itemconfig(timer_text , text="00:00")
    checkmark_label.config(text=" ")
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    print(f" Number of reps {REPS}")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 2 != 0:
        timer_label.config(text="Work" , fg=GREEN)
        count_down(work_sec)
    elif REPS % 2 == 0 and REPS != 8:
        timer_label.config(text="Break" , fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Break" , fg=RED)
        count_down(long_break_sec)
        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # change canvas text element using the itemconfig() method
    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000 , count_down, count -1)
    # start the timer again for another rep after previous rep is done counting
    else:
        start_timer()
        marks = " "
        work_sessions = REPS / 2
        for session in range(work_sessions):
            marks = "✔"  
        checkmark_label.config(text=marks , fg=GREEN)
        
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50 , bg=YELLOW)


timer_label = Label(text="Timer")
timer_label.config(fg=GREEN , bg=YELLOW , font=(FONT_NAME , 25 , "bold"))
timer_label.grid(column=1 , row=0)

# Create a canvas widget
## Canvas widget is used for 2D animations and drawings on the tkinter window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 

# Create an instance of a Photoimage class
## This class is used to read image files
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100 , 112 , image=tomato_img)

# Assign a variable to canvas.create_text to effect the countdown mechanism
timer_text = canvas.create_text(100 , 130  , text="00:00" , fill="white" , font=(FONT_NAME, 35 , "bold "))  
canvas.grid(column=1 ,row=1)

# Call the countdown function when start buttton is clicked to effect the countdown mechanism
start_button = Button(text="Start" , highlightthickness=0 , command=start_timer)
start_button.grid(column=0, row=2)

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