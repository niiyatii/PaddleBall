import tkinter as tk
import os

def callback():
    filename = 'PaddleBall.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('IDLE '+filename) #Open in notepad

root = tk.Tk()
tk.Button(root, text="Start", command=callback).pack()
root.mainloop()
