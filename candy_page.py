#giu to sort candy
import tkinter as tk
win =tk.Tk()
win.geometry('450x400')
win.configure(background='#e86c3f')

#function for the button picture
def corn():
    candy_name_label.configure(text='candy corn')
    #candy_photo_label.configure(image = 'candycorn_Photo')
    #nutrition_label.configure(image = 'candycorn_nut_Photo')

def twix():
    candy_name_label.configure(text='twix')
    #nutrition_label.configure(image = 'twix_nut_Photo')
     #candy_photo_label.configure(image = 'twix_Photo')


def milky_way():
    candy_name_label.configure(text='Milky way')
    #nutrition_label.configure(image = 'milky_way_nut_Photo')
     #candy_photo_label.configure(image = 'milky_way_Photo')

def crunch():
    candy_name_label.configure(text='crunch')
    #nutrition_label.configure(image = 'crunch_nut_Photo)
    #candy_photo_label.configure(image = 'crunch_Photo)


#adding photos of candy
#candycorn_Photo = tk.PhotoImage(files = '')
#twix_Photo = tk.PhotoImage(files = '')
#mily_way_Photo = tk.PhotoImage(files = '')
#crunch_Photo = tk.PhotoImage(files = '')\


candy_Frame = tk.Frame(win, background = '#e86c3f')
candy_Frame.pack()

candy_name_label = tk.Label(candy_Frame, text='', font = 'Times 12')
candy_name_label.grid(column=1,row =0)
#nutrition area
#nutrition photo
#twix_nut_Photo = tk.PhotoImage(files = '')
#milkyway_nut_Photo = tk.PhotoImage(files = '')
#crunch_nut_Photo = tk.PhotoImage(files = '')
#candy_corn_Photo = tk.PhotoImage(files = '')
#nutrition_label=tk.Label(candy_Frame)

#frame for the lists known



win.mainloop()