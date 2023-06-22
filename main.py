from tkinter import *
import math

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
WORK_REPS = 0
BREAK_REPS = 0
TIMER = None

# BRING WINDOW TO FRONT
def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

# RESET FUNCTION
def reset_timer():
    global REPS
    global WORK_REPS
    window.after_cancel(TIMER)
    REPS = 0
    WORK_REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    tick_marks.config(text='')
    message_label.config(text='')

# TIMER FUNCTION
def start_timer():
    global WORK_REPS
    if REPS == 8:
        reset_timer()
        return
    if WORK_REPS == 4:
        count_down(LONG_BREAK_MIN * 60)
        message_label.config(text='Enjoy your long break!')
    elif REPS % 2 == 0:
        message_label.config(text='')
        count_down(WORK_MIN * 60)
    elif REPS % 2 == 1:
        count_down(SHORT_BREAK_MIN * 60)
        message_label.config(text='Take a short break.')

# COUNT DOWN FUNCTION
def count_down(count):
    global REPS
    global WORK_REPS
    global TIMER

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    if count == 0 and REPS % 2 == 0:
        REPS += 1
        WORK_REPS += 1
        tick_marks.config(text=WORK_REPS * '✅')
        raise_above_all(window)
    elif count == 0 and REPS % 2 == 1:
        REPS += 1
        raise_above_all(window)
        
# GUI SETUP
# init window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# widgets
title_label = Label(text='Pomodoro Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0, sticky=(N))
btn_start = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
btn_start.grid(column=0, row=2, sticky=(E))
btn_reset = Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
btn_reset.grid(column=2, row=2, sticky=(W))
tick_marks = Label(text='', bg=YELLOW)
tick_marks.grid(column=1, row=3)
message_label = Label(text='', fg=PINK, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
message_label.grid(column=1, row=4)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=(tomato_img))
timer_text = canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

window.mainloop()
