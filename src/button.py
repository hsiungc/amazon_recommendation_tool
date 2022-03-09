from tkinter import *
from tkinter import messagebox
import datafile_connect

menu_select = Tk()

# Set sizes and placement of window
window_width = 300
window_height = 230
screen_width = menu_select.winfo_screenwidth()
screen_height = menu_select.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

menu_select.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
menu_select.title('Amazon BI Tool')

# Set menu
menuval = StringVar()
label = Label(menu_select, text = 'Amazon Product Menu\n', font = ('Arial', 15, 'bold'))
label.pack()

# Assign product name to variable
def pick_fp():
    global prodchoice
    prodchoice = 'French Press'
    menu_select.destroy()
    
def pick_tread():
    global prodchoice
    prodchoice = 'Treadmill'
    menu_select.destroy()

def pick_ws():
    global prodchoice
    prodchoice = 'Wine Stopper'
    menu_select.destroy()

# Closing protocol
def closing():
    if messagebox.askokcancel('Quit','Do you want to quit?'):
        menu_select.destroy()

# Product buttons
fpbutton = Button(menu_select, height = 2, width = 15,
                  text ="French Press", activebackground = 'black',
                  command = pick_fp)
fpbutton.pack(pady = 5)
tmbutton = Button(menu_select, height = 2, width = 15,
                  text ="Treadmill", activebackground = 'black',
                  command = pick_tread)
tmbutton.pack(pady = 5)
wsbutton = Button(menu_select, height = 2, width = 15,
                  text ="Wine Stopper", command = pick_ws)
wsbutton.pack(pady = 5)

menu_select.protocol("WM_DELETE_WINDOW", closing)

menu_select.mainloop()
