import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pathlib
from pathlib import Path
import shutil

def organize():
    subdirpath = []
    subdir = []
    filepath = filedialog.askdirectory()
    part1_text.set(filepath)
    
    Blank = []
    for output in os.listdir(filepath):
        Blank.append(output.split('.')[-1])
    Blank = list(dict.fromkeys(Blank))

    for ext in Blank:
        try:
            path = os.path.join(filepath, ext)
            subdirpath.append(path)
            path2 = path
            pong = path.split('/')
            subdir.append(pong[-1])
            os.mkdir(path2)
        except FileExistsError:
            continue

    for files in os.listdir(filepath):
        ending = (files.split('.')[-1])
        for x, y in enumerate(subdir):
            if ending == y:
                try:
                    needed = subdirpath[x]
                    needed = needed + '/' + files
                    source = filepath + '/' + files
                    os.rename(source, needed)
                except OSError:
                    continue
    
    print('Success?')

    
def quit():
    global app
    app.quit()

#Creates window
app = tk.Tk()

#Directory1
part1_text = StringVar()
part1_label= Label(app, text='Directory')
part1_label.grid(row = 0, column = 0, pady=10)
part1_entry = Entry(app, textvariable=part1_text, width = 40)
part1_entry.grid(row = 0, column = 1, pady=10)

#Button1
Confirm = Button(app, text="Open Directory", command = organize)
Confirm.grid(row = 0, column = 2, pady=10)

#Quit
Quit = Button(app, text = "Close", command = quit)
Quit.grid(row = 1, column = 0 , pady= 10)


#Defines window size
app.title('LogicFolder')
app.geometry('570x120')

#Starts program
app.mainloop()
