import tkinter as tk

win = tk.Tk()
win.title(" Remind Me ")
win.geometry("550x550")
win.configure(background="#e86c3f")

candyList = []
index = 0


def updateScreen():
    new_candy_entry.delete(0, "end")
    if len(candyList) > 0:
        output_label.configure(text=candyList[index])
        number_label.configure(text=index + 1)
    else:
        output_label.configure(text=" Add Candy ")


def addReminder():
    addInput = candy.get()
    candyList.append(addInput)
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
    updateScreen()




title_frame = tk.Frame(win, width=320, background="#e89cf3")
title_frame.pack()

welcome_label = tk.Label(title_frame, text=" Please add some candy", font="Georgia, 36", background="#e89cf3", foreground="#fff")
welcome_label.grid(row=0, column=0, ipadx=10)

output_frame = tk.Frame(win, width=320, background="#e89cf3")
output_frame.pack(pady=5)
output_label = tk.Label(output_frame, width=25, height=8, background="#e89cf3", borderwidth=2, relief="solid",font="Georgia 14")
output_label.grid(row=0, column=0)

button_frame = tk.Frame(win, width=320, background="#e89cf3")
button_frame.pack(pady=5)
back_photo = tk.PhotoImage(file='back_icon.png')
forward_photo = tk.PhotoImage(file='forward_icon.png')
back_button = tk.Button(button_frame, background="#e89cf3", image=back_photo, width=80, command=moveBack)
back_button.grid(row=0, column=0, padx=3)
number_label = tk.Label(button_frame, text="0", width=5, foreground="#fff", background="#e89cf3", font="Georgia 14")
number_label.grid(row=0, column=1, ipadx=30)
forward_button = tk.Button(button_frame, background="#e89cf3", image=forward_photo, width=80, command=moveForward)
forward_button.grid(row=0, column=2, padx=3)

input_frame = tk.Frame(win, width=320, background="#e89cf3")
input_frame.pack(pady=5)

candy = tk.StringVar()
new_candy_entry = tk.Entry(input_frame, textvariable=candy, background="#e89cf3", width=34)
new_candy_entry.grid(row=0, column=0, padx=7, ipady=10)
add_candy = tk.Button(input_frame, text="Add", background="#e89cf3", font="Georgia 14", command=addReminder)
add_candy.grid(row=0, column=1, padx=5)

clear_frame = tk.Frame(win, width=320, background="#e89cf3")
clear_frame.pack(pady=5)
clear_button = tk.Button(clear_frame, text=" Clear Screen ", background="#e89cf3", font="Georgia 14", command=clear)
clear_button.grid(row=0, column=1, ipadx=30)

win.mainloop()