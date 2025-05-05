import tkinter
import math
#TIP: better to use GRID instead of Pack layout manager
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeatitions = 0
clock_countdown = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_btn_clickled():
    window.after_cancel(clock_countdown)
    title_label.config(text="Timer",fg= GREEN)
    canvas.itemconfig(time_count, text = "00:00")
    check_mark_txt.config(text="...")
    global repeatitions
    repeatitions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repeatitions
    repeatitions+=1 
    time_25mins = WORK_MIN*60
    time_5mins = SHORT_BREAK_MIN*60
    time_20mins_break = LONG_BREAK_MIN*60

    if repeatitions == 8:
        count_down(time_20mins_break)
        title_label.config(text = 'Chill',fg=RED)
    elif repeatitions %2 == 0:
        count_down(time_5mins)
        title_label.config(text = 'Break',fg= PINK)
    else:
        count_down(time_25mins)
        title_label.config(text='Work',fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(time_min_in_secs):    
    mins = math.floor(time_min_in_secs/60)
    seconds = time_min_in_secs%60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(time_count, text = f'{mins}:{seconds}')
    if time_min_in_secs > 0:
        global clock_countdown
        clock_countdown = window.after(1000, count_down, time_min_in_secs-1)
    elif time_min_in_secs == 0:
        start_timer()
        global repeatitions
        marks = ""
        for x in range(int(repeatitions/2)):
            marks+= "✔"
        check_mark_txt.config(text=marks)
        


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro App')
window.minsize(width=500,height=400)
window.config(background =YELLOW)
window.config(padx=50,pady=30)

# Timer Text
title_label = tkinter.Label(text="Timer",bg= YELLOW,fg=GREEN,font= (FONT_NAME, 45, 'bold')) 
#fg is for foregroud color and bg for background color
title_label.grid(column=1,row=1)

# TOMATO Image
canvas = tkinter.Canvas(background=YELLOW, highlightthickness=0) #canvas class helps add img,color,text on our window
my_image = tkinter.PhotoImage(file='./Day28/tomato.png') #through photoimage class we identify the img to be placed on window
canvas.create_image(200,120, image = my_image)
time_count = canvas.create_text(205,135,text= '00:00',fill='white',font=(FONT_NAME, 30, 'bold')) #fill is like fg is color of text
canvas.grid(column=1,row=2)


# Start and Reset Button
start_btn  = tkinter.Button(text= 'Start',command= start_timer)#command = start_25min_timer
start_btn.grid(column=0,row=3)

reset_btn = tkinter.Button(text='Reset',command=reset_btn_clickled)
reset_btn.grid(column=2,row=3)

# Check Mark
check_mark_txt = tkinter.Label(text='...',bg= YELLOW,fg=GREEN,font=(FONT_NAME, 20, 'bold'))
check_mark_txt.grid(column=1,row=4)

# WHEN same BUTTON ARE PRESSED MULTIPLE TIMES ERROR IS GENERATED
key_request = tkinter.Label(text='(Recommended: please refrain from \npressing same button multiple times)',bg= YELLOW,fg=RED,font=(FONT_NAME, 10))
key_request.grid(column=1,row=5)

window.mainloop()