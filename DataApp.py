from tkinter import *
import tkinter as tk
from ctypes import windll
import random
windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()
frame = Frame(window)
window.title("Python Data App")
window.geometry("800x500")
icon = PhotoImage(file="PythonLogo.png")
window.iconphoto(True, icon)
name_var=tk.StringVar()

class character:
    def __init__(self):
        self.name = ""
        self.characterStats = {"strength": 0, "Intelligence": 0, "Constitution": 0, "Dexterity": 0, "Wisdom": 0, "Charisma": 0}



char = character()
characterParty = []

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

name_text = Label(stats_screen, text = "Name:").grid(row = 0, column = 1, padx =5, pady = 3)
strength_text = Label(stats_screen, text = "Strength:").grid(row = 1, column = 1, padx =5, pady =3)
int_text = Label(stats_screen, text = "Intelligence:").grid(row = 2, column = 1, padx = 5, pady = 3)
const_text = Label(stats_screen, text = "Constitution:").grid(row = 3, column = 1, padx = 5, pady = 3)
dex_text = Label(stats_screen, text = "Dexterity:").grid(row = 4, column = 1, padx = 5, pady = 3)
wisdom_text = Label(stats_screen, text = "Wisdom:").grid(row = 5, column = 1, padx = 5, pady =3)
char_text = Label(stats_screen, text = "Charisma").grid(row = 6, column = 1, padx = 5, pady = 3)

char1Label = Label(char_slot_1, text = "char1")
char1Label.grid(row = 0, column =1, padx = 5, pady =5)
char2Label = Label(char_slot_2, text = "char2")
char2Label.grid(row = 0, column =1, padx = 5, pady =5)
char3Label = Label(char_slot_3, text = "char3")
char3Label.grid(row = 0, column =1, padx = 5, pady =5)
char4Label = Label(char_slot_4, text = "char4")
char4Label.grid(row = 0, column =1, padx = 5, pady =5)

name_entry = tk.Entry(stats_screen,textvariable = name_var)
name_entry.grid(row = 0, column = 2, padx =5, pady =3)
strength_result_text = Label(stats_screen, text = "0")
strength_result_text.grid(row = 1, column = 2, padx = 5, pady = 3)
int_result_text = Label(stats_screen, text = "0")
int_result_text.grid(row = 2, column = 2, padx = 5, pady = 3)
const_result_text = Label(stats_screen, text = "0")
const_result_text.grid(row = 3, column = 2, padx = 5, pady = 3)
dex_result_text = Label(stats_screen, text = "0")
dex_result_text.grid(row = 4, column = 2, padx = 5, pady = 3)
wisdom_result_text = Label(stats_screen, text = "0")
wisdom_result_text.grid(row = 5, column = 2, padx = 5, pady = 3)
char_result_text = Label(stats_screen, text = "0")
char_result_text.grid(row = 6, column = 2, padx = 5, pady = 3)

def roll_stats():
    char.characterStats["strength"] = random.randint(0,5)
    strength_result_text.config(text = char.characterStats["strength"])

    char.characterStats["Intelligence"] = random.randint(0,5)
    int_result_text.config(text=char.characterStats["Intelligence"])

    char.characterStats["Constitution"] = random.randint(0, 5)
    const_result_text.config(text=char.characterStats["Constitution"])

    char.characterStats["Dexterity"] = random.randint(0, 5)
    dex_result_text.config(text=char.characterStats["Dexterity"])

    char.characterStats["Wisdom"] = random.randint(0, 5)
    wisdom_result_text.config(text=char.characterStats["Wisdom"])

    char.characterStats["Charisma"] = random.randint(0, 5)
    char_result_text.config(text=char.characterStats["Charisma"])

def submit():
    char.name = name_var.get()
def save():
    if (name_entry == ""):
        print("please enter a name")
    else:
        submit()
        char1Label.config(text = char.name)




        #add a loop to the save function to check for if a party slot is already full, if so then use second char slot, etc
        #if all slots are full, print out a message saying all slots are full
        #add a reset button that lets the player choose which party slot to reset





Button(window, text = "Roll Stats", command= roll_stats).grid(row=1, column = 1)
Button(window, text = "Save", command = save).grid(row=1, column = 2)
window.mainloop()