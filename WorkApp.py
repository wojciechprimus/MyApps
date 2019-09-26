#! python3
# Agent.py - This program is helping me to count what I learned today with Python. And are saving the content into .txt file

import tkinter as tk
from tkinter import *
import sys, os, time
from datetime import date ,datetime

today = date.today()

window = tk.Tk()
window.geometry('800x200+400+300')
window.title("Work App")

def help():
    print("This program is helping me to count what I learned today with Python. And are saving the content into .txt file")

def update_reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)

def dat():
    time_string = time.strftime("%D")
    dats.config(text=time_string)
    dats.after(200, tick)

def writer():
    start = e1.get()
    finish = e2.get()
    FMT = '%H:%M:%S'
    dif = datetime.strptime(finish, FMT) - datetime.strptime(start, FMT)

    f=open("workingtime.txt", "a+")
    f.write("\nDate: %s Start_time: %s Finish_time: %s Work_time %s Topic: %s" % (today,
                                e1.get(),
                                e2.get(),
                                dif,
                                e3.get()))
    f.close()

def study():
    f=open("workingtime.txt", "r+")
    oneline = f.readline()
    numb = re.compile(r'[\d\d:\d\d:\d\d\d$]')
    first = numb.findall(oneline)
    fir.config(text=first)
    fir.after(200, tick)
    f.close()

def show():
    filepath = 'workingtime.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        show = e4.get()
        print(show)
        while line:
            if show in line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
            else:
                pass
                line = fp.readline()
                cnt += 1

clock=Label(window, font=("times", 15, "bold"), bg= "gray")
clock.grid(row=7, column=2)

dats=Label(window, font=("times", 15, "bold"), bg= "gray")
dats.grid(row=7, column=0)

fir=Label(window, font=("times", 15 , "bold"), bg= "gray")
fir.grid(row=7, column=3)

menu = Menu(window)
window.config(menu=menu)

filename = Menu(menu)
menu.add_cascade(label='File', menu=filename)

filename.add_command(label='New', command = update_reset)
filename.add_command(label='Exit', command = quit)

menu.add_cascade(label='Help', command=help)

tk.Label(window, text="Write a content inside:").grid(row=0,column=2)
tk.Label(window, text="Read a line from a specific date").grid(row=0,column=3)
tk.Label(window, text="(write it in the order yyyy-mm-dd):").grid(row=1,column=3)

tk.Label(window, text="When Did You start the lesson(HH:MM:SS)").grid(row=1, column=0)
tk.Label(window, text="When Did You finish the lesson(HH:MM:SS)").grid(row=2, column=0)
tk.Label(window, text="What was the Topic").grid(row=3, column=0)
tk.Label(window, text="Current Date").grid(row=6, column=0)
tk.Label(window, text="Current time").grid(row=6, column=2)
tk.Label(window, text="Study time in Total").grid(row=6, column=3)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)


e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=2, column=3)

tk.Button(window,
          text='Show a content from a specific date',
          command=show).grid(row=3,
                                    column=3,
                                    sticky=tk.W)
tk.Button(window,
          text='SAVE the content into a file', command=writer).grid(row=5,
                                                       column=3,
                                                       sticky=tk.W,
                                                       pady=4)

tick()
dat()
study()

window.mainloop()
