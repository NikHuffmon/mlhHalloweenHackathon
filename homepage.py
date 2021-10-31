import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import random
from tkinter import messagebox

win = tk.Tk()

mainFrame=tk.Frame(win, background='#e86c3f')
mainFrame.grid(column=0,row=0)
'''
win = Toplevel()
win.title(" Remind Me ")
win.geometry("550x550")
win.configure(background="#e86c3f")
'''
candyList = []
index = 0
#candyText = 'Please enter in a type of candy'
candy = tk.StringVar()
candy.set('Please enter in a type of candy')
candies_list = ['Sugary','Sweet','Chocolate']

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
addInput = candy.get()
candyTypes = ['Chocolate','Sugary','Sweet','chocolate','sugary','sweet']
def addReminder():
    print(candy.get())
    for i in candyTypes:
        print(candyTypes)
        print(i)
        Poob = 0
        if i == candy.get():
            Poob = 1
            print('happy')         
            addInput = candy.get()
            candyList.append(addInput)
            
            new_candy_entry.delete(0,'end')
            new_candy_entry.insert(0,'Please enter in another candy type')
            win.focus()
        if i == candyTypes[5] and i != candy.get() and i != candy.get() and Poob != 1:
            messagebox.showerror('Please enter in a valid choice of candy from the choices on the right')
            new_candy_entry.delete(0,'end')
            new_candy_entry.insert(0,'Please enter in another candy type')  
            win.focus()
      #  elif i !=candy.get():
          #  print('sad')

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
    output_label.configure(text=" Add Candy ")
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
def provideInfo():
    messagebox.showinfo('Information','Please enter in a type of candy shown from the list to the right. Then click add. \n\n Once complete click the add button. \n\n If you have multiple different candies to add, please enter in another piece of candy and click add again. \n\n If you would like to see all the candies you have entered, please click on the arrow boxes and you will be shown with all the differnet candies you have entered.')

def createNewWindow():
    if candyList == []:
        messagebox.showerror('Please enter in a type of candy')
    else:
        mainFrame.grid_forget()
        candy_information_frame.pack()
        test()

  
# -------------------------------------------------------------------->
# Chase's information/code
#function for the button picture
candy_information_frame = tk.Frame(win)
candy_information_frame.grid_forget()

candyEntryLabel = tk.Label(candy_information_frame,text='Please select a candy from the choices below',font = 'Georgia 14',background='#e86c3f')
candyEntryLabel.pack()
candyListItems = ''
interestLabel = tk.Label(candy_information_frame,text='')
interestLabel.pack()
def test():
    global candyListItems
    print('hello')
    for i in candyList:
        candyListItems = i
        print(candyListItems)
        interestLabel.configure(text='We see you are interested in '+candyListItems)
     
requestLabel = tk.Label(candy_information_frame,text='Please chose from the choices below to see the nutriental value and images of a similar type of candy to your generic choice chosen')
requestLabel.pack()

candy_Frame = tk.Frame(candy_information_frame, background = '#e86c3f')
candy_Frame.pack()

candy_name_label = tk.Label(candy_Frame, text='', font = 'Times 12')
candy_name_label.grid(column=1,row =0)

radioFrame = tk.Frame(candy_information_frame)
radioFrame.pack()

radVar = tk.IntVar()

candyCorn = tk.Radiobutton(radioFrame,variable=radVar, text='Chocolate',background='#e86c3f',value=1)
candyCorn.pack()

#Chocolate
twix = tk.Radiobutton(radioFrame,variable=radVar,text='Twix',background='#e86c3f',value=2)
twix.pack()

milkyWay = tk.Radiobutton(radioFrame,variable=radVar,text='Milk Way',background='#e86c3f',value=3)
milkyWay.pack()

crunch = tk.Radiobutton(radioFrame,variable=radVar,text='Crunch',background='#e86c3f',value=4)
crunch.pack()

#Photo Frame
candyPhoto = tk.Frame(candy_information_frame)
candyPhoto.pack()

#adding photos of candy
candycorn_Photo = tk.PhotoImage(file = 'candyCorn.png')
twix_Photo = tk.PhotoImage(file = 'twix.png')
milky_way_Photo = tk.PhotoImage(file = 'milkyWay.png')
crunch_Photo = tk.PhotoImage(file = 'crunch.png')
jelly_Photo = tk.PhotoImage(file='jellyBeans.png')

candyCornPhoto = tk.Label(candyPhoto,image=candycorn_Photo,width=200,height=200)
candyCornPhoto.pack_forget()

twixPhoto = tk.Label(candyPhoto,image=twix_Photo,width=800,height=400)
candyCornPhoto.pack_forget()

milkWayPhoto = tk.Label(candyPhoto,image=milky_way_Photo,width=800,height=400)
milkWayPhoto.pack_forget()

crunchPhoto = tk.Label(candyPhoto,image=crunch_Photo,width=800,height=400)
crunchPhoto.pack_forget()

jellyPhoto = tk.Label(candyPhoto,image=jelly_Photo,width=200,height=400)
jellyPhoto.pack_forget()

#nutrition area
#nutrition photo
#twix_nut_Photo = tk.PhotoImage(files = '')
#milkyway_nut_Photo = tk.PhotoImage(files = '')
#crunch_nut_Photo = tk.PhotoImage(files = '')
#candy_corn_Photo = tk.PhotoImage(files = '')
#nutrition_label=tk.Label(candy_Frame)

#frame for the lists known

#End of Chase's code
#-------------------------------------------------------------------------->


list_of_candies = tk.Frame(mainFrame,background='#e86c3f')
list_of_candies.pack(side=RIGHT)

candyGeneric = tk.Label(list_of_candies,text='Available candies',background='#e86c3f',font='Georgia 18 bold')
candyGeneric.pack()

sugar_label=tk.Label(list_of_candies,text='',background='#e86c3f',font='Georgia 14')
sugar_label.pack()

sweet_label=tk.Label(list_of_candies,text='',background='#e86c3f',font='Georgia 14')
sweet_label.pack()

chocolate_label = tk.Label(list_of_candies,text='',background='#e86c3f',font='Georgia 14')
chocolate_label.pack()


f= True

while f:
    for i in candies_list:
        if i == candies_list[2]:
            chocolate_label.configure(text=i)    
            f = False
        if i == candies_list[1]:
            sweet_label.configure(text=i)
            f = False
        if i == candies_list[0]:
           sugar_label.configure(text=i)
           f= False
           print(i)
    


#Creating Menu Bar
menuBar = Menu(mainFrame)
win.config(menu=menuBar)
#File menu
fileMenu = Menu(menuBar,tearoff=0)
fileMenu.add_command(label='Information',command=provideInfo)
menuBar.add_cascade(label='How to operate',menu=fileMenu)

title_frame = tk.Frame(mainFrame, width=320, background="#e86c3f")
title_frame.pack()

welcome_label = tk.Label(title_frame, text=" Please add some candy", font="Georgia, 36", background="#e86c3f", foreground="#fff")
welcome_label.grid(row=0, column=0, ipadx=10)

information_frame = tk.Frame(mainFrame,background='#e86c3f')
information_frame.pack()

information_label = tk.Label(information_frame, text='')


output_frame = tk.Frame(mainFrame, width=320, background="#e86c3f")
output_frame.pack(pady=5)
output_label = tk.Label(output_frame, width=25, height=8, background="#e86cf3", borderwidth=2, relief="solid",font="Georgia 14")
output_label.grid(row=0, column=0)

button_frame = tk.Frame(mainFrame, width=320, background="#e86c3f")
button_frame.pack(pady=5)

back_photo = tk.PhotoImage(file='back_icon.png')
forward_photo = tk.PhotoImage(file='forward_icon.png')
back_button = tk.Button(button_frame, background="#e86cf3", image=back_photo, width=80, command=moveBack)
back_button.grid(row=0, column=0, padx=3)

number_label = tk.Label(button_frame, text="0", width=5, foreground="#fff", background="#e86cf3", font="Georgia 14")
number_label.grid(row=0, column=1, ipadx=30)

forward_button = tk.Button(button_frame, background="#e86cf3", image=forward_photo, width=80, command=moveForward)
forward_button.grid(row=0, column=2, padx=3)

input_frame = tk.Frame(mainFrame, width=320,background='#e86c3f')
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

clear_frame = tk.Frame(mainFrame, width=320, background="#e86cf3")
clear_frame.pack(pady=5)

clear_button = tk.Button(clear_frame, text=" Clear Screen ", background="#e86cf3", font="Georgia 14", command=clear)
clear_button.grid(row=0, column=1, ipadx=30)

next_window = tk.Frame(mainFrame, background='#e86c3f')
next_window.pack()

next_window_button = tk.Button(next_window, text='Next', background='#e86cf3',font='Georgia 14',command=createNewWindow)
next_window_button.grid(column=0,row=0)

win.mainloop()