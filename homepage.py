import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import random

win = tk.Tk()
win.title(" Remind Me ")
win.geometry("550x550")
win.configure(background="#e86c3f")

candyList = []
index = 0
#candyText = 'Please enter in a type of candy'
candy = tk.StringVar()
candy.set('Please enter in a type of candy')

billy = True
'''
while true:
    candy.set(candyText)

'''


whatsFocused = win.focus_get

def updateScreen():
   # new_candy_entry.delete(0, "end")
    if len(candyList) > 0:
        output_label.configure(text=candyList[index])
        number_label.configure(text=index + 1)
    else:
        output_label.configure(text=" Add Candy ")


def addReminder():
    addInput = candy.get()
    candyList.append(addInput)
    new_candy_entry.delete(0,'end')
    new_candy_entry.insert(0,'Please enter in another candy type')
   # print(new_candy_entry.get())
    #global candyList
    #global index

    #candyList= []
    #index = 0
    #number_label.configure(text="")
  #  win.focus()
    #number_label.config(text='0')
    #testVar.set(candyText)
  #  if candy == candy.get():
  #      print('hello')

  #  new_candy_entry.insert(0,'Please enter in another candy type')
  #  print(new_candy_entry.get())
    clicked = new_candy_entry.bind('<Button-1>',click)  
    updateScreen()


def moveForward():
    global index
    if index < len(candyList) - 1:
        index = index + 1
    updateScreen()


def moveBack():
    global index
    if index > 0:
        index = index - 1
    updateScreen()


def clear():
    global candyList
    global index

    candyList= []
    index = 0
    number_label.configure(text="")
    win.focus()
    number_label.config(text='0')
    #testVar.set(candyText)
    if candy == candy.get():
        print('hello')
    if candy.get() != 'Please enter in another candy type':
        new_candy_entry.delete(0,'end')
        new_candy_entry.insert(0,'Please enter in another candy type')
   # if new_candy_entry.get() != 'Please enter in another candy type':
    #    new_candy_entry.insert(0,'Please enter in another candy type')

    #new_candy_entry.insert(0,'Please enter in another candy type')
    #if candy.get() == 'Please enter in another candy typePlease enter in another candy type':
     #   new_candy_entry.delete(0,'end')
     #   new_candy_entry.insert(0,'Please enter in another candy type')
     #   print('hello')
    #print(new_candy_entry.get())
    clicked = new_candy_entry.bind('<Button-1>',click)    
    


    
def setTextInput(text):
    new_candy_entry.insert(0,text)
    
    
    updateScreen()

def click(event):
    print('hello')
    new_candy_entry.configure(state=NORMAL)
    new_candy_entry.delete(0,'end')

    new_candy_entry.unbind('<Button-1>',clicked)
    '''
    if new_candy_entry == '.!frame5.!entry ':
        new_candy_entry.config(text='hello')
        print('ehll')
    else:
        print('test12345')
        print(new_candy_entry)
        new_candy_entry.config(text='PLEASE')
        label=tk.Label(win,text=new_candy_entry,foreground='#000')
        label.pack()
    
'''



title_frame = tk.Frame(win, width=320, background="#e86c3f")
title_frame.pack()

welcome_label = tk.Label(title_frame, text=" Please add some candy", font="Georgia, 36", background="#e86c3f", foreground="#fff")
welcome_label.grid(row=0, column=0, ipadx=10)

information_frame = tk.Frame(win,background='#e86c3f')
information_frame.pack()

information_label = tk.Label(information_frame, text='')


output_frame = tk.Frame(win, width=320, background="#e86c3f")
output_frame.pack(pady=5)
output_label = tk.Label(output_frame, width=25, height=8, background="#e86cf3", borderwidth=2, relief="solid",font="Georgia 14")
output_label.grid(row=0, column=0)

button_frame = tk.Frame(win, width=320, background="#e86c3f")
button_frame.pack(pady=5)

back_photo = tk.PhotoImage(file='back_icon.png')
forward_photo = tk.PhotoImage(file='forward_icon.png')
back_button = tk.Button(button_frame, background="#e86cf3", image=back_photo, width=80, command=moveBack)
back_button.grid(row=0, column=0, padx=3)

number_label = tk.Label(button_frame, text="0", width=5, foreground="#fff", background="#e86cf3", font="Georgia 14")
number_label.grid(row=0, column=1, ipadx=30)

forward_button = tk.Button(button_frame, background="#e86cf3", image=forward_photo, width=80, command=moveForward)
forward_button.grid(row=0, column=2, padx=3)

input_frame = tk.Frame(win, width=320,background='#e86c3f')
input_frame.pack(pady=5)


new_candy_entry = ttk.Entry(input_frame, textvariable=candy, background="#e86cf3", width=34)
new_candy_entry.grid(row=0, column=0, padx=7, ipady=10)

#if  whatsFocused != new_candy_entry:
#        candy.set(candyText)
#elif whatsFocused == win:
#        candy.set(candyText)



clicked = new_candy_entry.bind('<Button-1>',click)

add_candy = tk.Button(input_frame, text="Add", background="#e86cf3", font="Georgia 14", command=addReminder)
add_candy.grid(row=0, column=1, padx=15)

clear_frame = tk.Frame(win, width=320, background="#e86cf3")
clear_frame.pack(pady=5)

clear_button = tk.Button(clear_frame, text=" Clear Screen ", background="#e86cf3", font="Georgia 14", command=clear)
clear_button.grid(row=0, column=1, ipadx=30)

next_window = tk.Frame(win, background='#e86c3f')
next_window.pack()

next_window_button = tk.Button(next_window, text='Next', background='#e86cf3',font='Georgia 14')
next_window_button.grid(column=0,row=0)
win.mainloop()