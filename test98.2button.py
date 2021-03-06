
import tkinter as tk
#from tkinter import *
def write_slogan():
    print("tkinter is easy to use")
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text="QUIT",fg="green",bg="red",command=quit)
button.pack(side=tk.LEFT)
slogan=tk.Button(frame,text="HELLO",command=write_slogan)
slogan.pack(side=tk.LEFT)
root.mainloop()
