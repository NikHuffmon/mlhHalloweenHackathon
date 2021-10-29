print('This is a test file')

print('tesasdfasdft')

print('I\'m praying')

print('Please')
print('hello')
import tkinter as tk

win = tk.Tk()
win.configure(background="#e89c3f")
win.geometry("500x500")

def labelChanage():
    finalChange = change.get()
    welcome_entry.configure(win, text=f"{finalChange}")
welcome_frame = tk.Frame(win, )
welcome_frame.grid(row=0, column=0)
welcomeLaBEL = tk.Label(welcome_frame, text=" Welocome to CSA wich stands for The Candy Sorter App ", foreground="#000", background="#e89c3f", font=" Georiga 14")
welcomeLaBEL.grid(row= 0, column=0)

entry_frame = tk.Frame(win, )
entry_frame.grid(row=1, column=0)
change = tk.StringVar
welcome_entry = tk.Entry(entry_frame, text="", textvariable=change)
welcome_entry.grid(row= 1, column=1)

win.mainloop()
