#gui to sort candy
import tkinter as tk
from tkinter import font
win = tk.Tk()
win.geometry('450x400')
win.configure(background ='#e86c3f')

#function for the button picture
#
candy_List=[]
index=0

candy_Frame = tk.Frame(win, background = '#e86c3f')
candy_Frame.pack()

candy_name_label = tk.Label(candy_Frame , text='Hi' , font='Times 12' , background = '#e86c3f')
candy_name_label.grid(column=0 , row=0)

win.mainloop()