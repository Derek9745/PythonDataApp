from tkinter import *
import tkinter as tk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()
frame = Frame(window)
window.title("Python Data App")
window.geometry("1200x900")
icon = PhotoImage(file="PythonLogo.png")
window.iconphoto(True, icon)
name_var=tk.StringVar()

def submit():
    name = name_var.get()


left_frame = Frame(window, width = 200, height = 400, bg = "grey")
left_frame.grid(row = 0, column = 0,padx = 10, pady = 5)

right_frame = Frame(window, width =650, height= 400, bg = "grey")
right_frame.grid(row=0,column=1, padx =10, pady=5)

stats_screen = Frame(right_frame, width = 650, height = 400)
stats_screen.grid(row = 2,column=1, padx=5, pady=5)

char_slot_1 = Frame(left_frame, width = 180, height = 185)
char_slot_1.grid(row = 2, column = 0, padx=5,pady=5)

char_slot_2 = Frame(left_frame, width = 180, height = 185)
char_slot_2.grid(row = 3, column = 0, padx=5,pady=5)

char_slot_3 = Frame(left_frame, width = 180, height = 185)
char_slot_3.grid(row = 4, column = 0, padx=5,pady=5)

char_slot_4 = Frame(left_frame, width = 180, height = 185)
char_slot_4.grid(row = 5, column = 0, padx=5,pady=5)

Label(right_frame, text ="Character Stats Creator").grid(row = 0, column = 1, padx =5, pady =5)
Label(left_frame, text="Character Party").grid(row = 1, column=0, padx=5,pady=5)

rollStats = Button(window, text = "Roll Stats").grid(row=1, column = 1)
saveStats = Button(window, text = "Save").grid(row=1, column = 2)

name_text = Label(stats_screen, text = "Name:").grid(row = 0, column = 1, padx =5, pady = 3)
strength_text = Label(stats_screen, text = "Strength:").grid(row = 1, column = 1, padx =5, pady =3)
int_text = Label(stats_screen, text = "Intelligence:").grid(row = 2, column = 1, padx = 5, pady = 3)
const_text = Label(stats_screen, text = "Constitution:").grid(row = 3, column = 1, padx = 5, pady = 3)
dex_text = Label(stats_screen, text = "Dexterity:").grid(row = 4, column = 1, padx = 5, pady = 3)
wisdom_text = Label(stats_screen, text = "Wisdom:").grid(row = 5, column = 1, padx = 5, pady =3)
char_text = Label(stats_screen, text = "Charisma").grid(row = 6, column = 1, padx = 5, pady = 3)

name_entry = tk.Entry(stats_screen,textvariable = name_var).grid(row = 0, column = 2, padx =5, pady =3)
strength_result_text = Label(stats_screen, text = "0").grid(row = 1, column = 2, padx = 5, pady = 3)
int_result_text = Label(stats_screen, text = "0").grid(row = 2, column = 2, padx = 5, pady = 3)
const_result_text = Label(stats_screen, text = "0").grid(row = 3, column = 2, padx = 5, pady = 3)
dex_result_text = Label(stats_screen, text = "0").grid(row = 4, column = 2, padx = 5, pady = 3)
wisdom_result_text = Label(stats_screen, text = "0").grid(row = 5, column = 2, padx = 5, pady = 3)
char_result_text = Label(stats_screen, text = "0").grid(row = 6, column = 2, padx = 5, pady = 3)
window.mainloop()