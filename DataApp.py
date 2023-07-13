from tkinter import *
import tkinter as tk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

window = tk.Tk()
window.title("Python Data App")
window.geometry("800x500")
title_label = tk.Label(master = window, text ="Data Analysis", font = "Calibri 12 bold")
title_label.pack()
icon = PhotoImage(file="PythonLogo.png")
window.iconphoto(True, icon)
window.mainloop()
