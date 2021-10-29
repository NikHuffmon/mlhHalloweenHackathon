#giu to sort candy
import tkinter as tk
win =tk.Tk()
win.geometry('450x400')
win.configure(background='#e86c3f')

#function for the button picture

#adding photos of candy
#candycorn_Photo = tk.PhotoImage(files = '')
#twix_Photo = tk.PhotoImage(files = '')
#mily_way_Photo = tk.PhotoImage(files = '')
#crunch_Photo = tk.PhotoImage(files = '')
candylist = []
index = 0

candy_Frame = tk.Frame(win, background = '#e86c3f')
candy_Frame.pack()

candy_name_label = tk.Label(candy_Frame, text='', font = 'Times 12')
candy_name_label.grid(column=1,row =0)
#nutrition area
#nutrition_label=tk.Label(candy_Frame)

#frame for the list

win.mainloop()