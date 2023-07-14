from tkinter import *
import tkinter as tk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()
frame = Frame(window)
window.title("Python Data App")
window.geometry("800x500")
icon = PhotoImage(file="PythonLogo.png")
window.iconphoto(True, icon)

#title_label = tk.Label(master = window, text ="Character Stats Creator", font = "Calibri 12 bold")


left_frame = Frame(window, width = 200, height = 400, bg = "grey")
left_frame.grid(row = 0, column = 0,padx = 10, pady = 5)


right_frame = Frame(window, width =650, height= 400, bg = "grey")
right_frame.grid(row=0,column=1, padx =10, pady=5)

stats_screen = Frame(right_frame, width = 650, height = 400)
stats_screen.grid(row = 2,column=1, padx=5, pady=5)



nav_bar = Frame(left_frame, width = 180, height = 185)
nav_bar.grid(row = 2, column = 0, padx=5,pady=5)

Label(right_frame, text ="Character Stats Creator").grid(row = 0, column = 1, padx =5, pady =5)
Label(left_frame, text="Character Party").grid(row = 1, column=0, padx=5,pady=5)
window.mainloop()