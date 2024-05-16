from tkinter import *
import math

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


# ----------------------------> TIMER RESET <------------------------------- #

def reset_button():
    global REPS

    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    check_label.config(text="")
    timer_label.config(text="Timer", foreground=GREEN, background=YELLOW)


# ----------------------------> TIMER <------------------------------- #


def start_function():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", foreground=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", foreground=GREEN)


# ----------------------------> COUNTDOWN <------------------------------- #


def count_down(count):
    global REPS
    global TIMER

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Dynamic Typing >> A variable that starts as an int for example can be modified into a string
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_function()
        marks = ""
        work_session = math.floor(REPS / 2)
        for n in range(work_session):
            marks += "✅"
        check_label.config(text=marks)


# ----------------------------> UI <------------------------------- #

window = Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, background=YELLOW)

# ADDING THE IMAGE TO THE WINDOW

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Adding text to the image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# Placing the image on the window
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 50), foreground=GREEN, background=YELLOW)
timer_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", background=YELLOW, font=(FONT_NAME, 20), foreground=GREEN, highlightthickness=0,
                      command=start_function)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", background=YELLOW, font=(FONT_NAME, 20), foreground=GREEN, highlightthickness=0,
                      command=reset_button)
reset_button.grid(column=2, row=2)

# Checkmark Label
check_label = Label(background=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
