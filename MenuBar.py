import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys
import os

window = tk.Tk()
window.geometry('550x200+400+300')
window.title("Menu BAR")

def help():
    print("This program is helping You to count how much money You will spend for a dinner.")

def update_reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def show_order():
    print("Apperitiv: %s\nMain Dish: %s\nDessert: %s\nDrink: %s" % (combo.get() + " " + e1.get()+" Times",
                                                                    combo2.get() + " " + e2.get()+" Times",
                                                                    combo3.get() + " " + e3.get()+" Times",
                                                                    combo4.get() + " " + e4.get()+" Times"))

def count_price():
    print("The Whole Price is:")
    b = (apperitiv.get(combo.get())*int(e1.get())+
              maindish.get(combo2.get())*int(e2.get())+
              dessert.get(combo3.get())*int(e3.get())+
              drink.get(combo4.get())*int(e4.get()))
    print(round(b, 2))

def count():
    a = int(e5.get()) - (apperitiv.get(combo.get())*int(e1.get())+
              maindish.get(combo2.get())*int(e2.get())+
              dessert.get(combo3.get())*int(e3.get())+
              drink.get(combo4.get())*int(e4.get()))
    print("The rest of Yours money after shopping is: ",round(a, 2))

apperitiv = {'Chips':1.50,'Bread':2.50,'Toast':1.10,'Nuts':1.80 ,'Salat':2.50}
maindish = {'Hamburger':3.00, 'Cheeseburger':3.20, 'Chicken':5.00, 'Pizza':4.50, 'Spaghetti':3.50}
dessert = {'Ice Cream':0.50, 'Snack':0.80, 'Chocolate Bar':0.30, 'Moussou':0.90, 'Pudding':1.20}
drink = {'Coca Cola':2.20,'Pepsi':2.10, 'Tea':1.50, 'Coffee':1.20, 'Beer':1.10}

menuBar = Menu(window)
window.config(menu=menuBar)

filename = Menu(menuBar)
menuBar.add_cascade(label='File', menu=filename)

filename.add_command(label='New', command = update_reset)
filename.add_command(label='Exit', command = quit)

menuBar.add_cascade(label='Help', command=help)

tk.Label(window, text="Select the Count").grid(row=0, column=3)
tk.Label(window, text="Select the Product").grid(row=0,column=2)
tk.Label(window, text="How Much You can pay:").grid(row=0,column=4)

tk.Label(window, text="Apperitiv").grid(row=1, column=0)
tk.Label(window, text="Main Dish").grid(row=2, column=0)
tk.Label(window, text="Dessert").grid(row=3, column=0)
tk.Label(window, text="Drink").grid(row=4, column=0)

combo = ttk.Combobox(window)
combo.grid(row=1, column=2)
combo.config(value=('Chips','Bread','Toast','Nuts','Salat'))
combo.set('Bread')

combo2 = ttk.Combobox(window)
combo2.grid(row=2, column=2)
combo2.config(value=('Hamburger', 'Cheeseburger', 'Chicken', 'Pizza', 'Spaghetti'))
combo2.set('Hamburger')

combo3 = ttk.Combobox(window)
combo3.grid(row=3, column=2)
combo3.config(value=('Ice Cream', 'Snack', 'Chocolate Bar', 'Moussou', 'Pudding'))
combo3.set('Ice Cream')

combo4 = ttk.Combobox(window)
combo4.grid(row=4, column=2)
combo4.config(value=('Coca Cola', 'Pepsi', 'Tea', 'Coffee', 'Beer'))
combo4.set('Coca Cola')

tk.Button(window,
          text='Quit',
          command=window.quit).grid(row=5,
                                    column=1,
                                    sticky=tk.W)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)
e5 = tk.Entry(window)

e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
e3.grid(row=3, column=3)
e4.grid(row=4, column=3)
e5.grid(row=1, column=4)

tk.Button(window,
          text='Show the Order', command=show_order).grid(row=5,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)
tk.Button(window,
          text='Count the Price', command=count_price).grid(row=5,
                                                       column=3,
                                                       sticky=tk.W,
                                                       pady=4)

tk.Button(window,
          text='Rest after shopping', command=count).grid(row=5,
                                                       column=4,
                                                       sticky=tk.W,
                                                       pady=4)

window.mainloop()
