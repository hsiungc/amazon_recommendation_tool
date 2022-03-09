from tkinter import *

summwindow = Tk()

# Set sizes and placement of window
summ_width = 400
summ_height = 800
center_width = summwindow.winfo_screenwidth()
center_height = summwindow.winfo_screenheight()
center_x = int(center_width/2 - summ_width / 2)
center_y = int(center_height/2 - summ_height / 2)

summwindow.geometry(f'{summ_width}x{summ_height}+{center_x}+{center_y}')
summwindow.resizable(0, 0)
summwindow.title('Amazon BI Product Summary Statistics')


container = Frame(summwindow)

canvas = Canvas(container)
scrollbar = Scrollbar(container, orient = 'vertical', command = canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind('<Configure>',
                      lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

canvas.create_window((0,0), window = scrollable_frame, anchor='nw')

canvas.config(width = 380, height = 625, yscrollcommand = scrollbar.set)
scrollbar.config(command = canvas.yview)

# Close menu function
def quit():
    print('Thank you for using the Amazon BI Tool!')
    summwindow.destroy()

# Closing protocol
def closing():
    if messagebox.askokcancel('Quit','Do you want to quit?'):
        summwindow.destroy()
        
# Set labels
titlelabel = Label(summwindow, text = '\n' + prodchoice,font = 'Arial 25 bold')
titlelabel.grid(row = 1, column = 0, columnspan = 2, pady = 2)
titlelabel.config(foreground = 'purple')

analyslabel = Label(summwindow, text = '\nProduct Summary Statistics',
                    font = 'Arial 16 bold')
analyslabel.grid(row = 2, column = 0, columnspan = 2, pady = 2)

# Price range
pricerange = Label(scrollable_frame, text = f'Price range:',  font = 'Arial 15 bold',
                   wraplength = 100, justify = CENTER)
pricerange.grid(row = 3, column = 0, columnspan = 1, padx = 2, pady = 5)
pricerange.config(foreground = 'blue')
pricerngscor = Label(scrollable_frame, text = f'{summarystats.price_range()}',
                     font = 'Arial 15')
pricerngscor.grid(row = 3, column = 1, columnspan = 1, padx = 2, pady = 5)

# Median price
pricemed = Label(scrollable_frame, text = f'Median price:',font = 'Arial 15 bold',
                 wraplength = 100, justify = CENTER)
pricemed.grid(row = 4, column = 0, columnspan = 1, padx = 2, pady = 5)
pricemedscor = Label(scrollable_frame, text = f'{summarystats.price_median()}',
                     font = 'Arial 15')
pricemed.config(foreground = 'blue')
pricemedscor.grid(row = 4, column = 1, columnspan = 1, padx = 2, pady = 5)

# Seller type
sellertype = Label(scrollable_frame, text = f'% of products sold by Amazon \
                    (including Amazon Brand):', 
                    font = 'Arial 15 bold', wraplength = 175, justify = CENTER)
sellertype.grid(row = 5, column = 0, columnspan = 1, padx = 2, pady = 5)
sellertype.config(foreground = 'blue')
sellertypescor = Label(scrollable_frame, text = f'{summarystats.sellertype()}',
                       font = 'Arial 15')
sellertypescor.grid(row = 5, column = 1, columnspan = 1, padx = 2, pady = 5)

# Ratings
ratings = Label(scrollable_frame, text = f'Average overall customer star rating:', 
                 font = 'Arial 15 bold', wraplength = 150, justify = CENTER)
ratings.grid(row = 6, column = 0, columnspan = 1, padx = 2, pady = 8)
ratings.config(foreground = 'blue')
ratingscor = Label(scrollable_frame, text = f'{summarystats.overall_rating()}',
                   font = 'Arial 15')
ratingscor.grid(row = 6, column = 1, columnspan = 1, padx = 2, pady = 5)

# Number of Reviews
numreviews = Label(scrollable_frame, text = f'Average # of reviews for top 10 \
                    products:', font = 'Arial 15 bold', wraplength = 130,
                   justify = CENTER)
numreviews.grid(row = 7, column = 0, columnspan = 1, padx = 2, pady = 8)
numreviews.config(foreground = 'blue')
numrevscor = Label(scrollable_frame, text = f'{summarystats.top_prod_avgrev()}',
                   font = 'Arial 15')
numrevscor.grid(row = 7, column = 1, columnspan = 1, padx = 2, pady = 5)

# All rankings
dobetter = Label(scrollable_frame, text = f'Total cumulative rankings by tier:',
                 wraplength = 170, font = 'Arial 15 bold', justify=CENTER)
dobetter.grid(row = 8, column = 0, columnspan = 1, padx = 2, pady = 10)
dobetter.config(foreground = 'blue')
dobetscor = Label(scrollable_frame, text = f'{addstats.get_total_best_sell()}',
                  font = 'Arial 15', wraplength = 200, justify = LEFT)
dobetscor.grid(row = 8, column = 1, columnspan = 1, padx = 2, pady = 10)

# Negative review keywords
negkw = Label(scrollable_frame, text = f'Top negative keywords:',
              font = 'Arial 15 bold', wraplength = 170, justify = CENTER)
negkw.grid(row = 9, column = 0, columnspan = 1, padx = 2, pady = 10)
negkw.config(foreground = 'blue')
negscor = Label(scrollable_frame, text = f'{summarystats.get_sum_negkw()}',
                font = 'Arial 15', wraplength = 200)
negscor.grid(row = 9, column = 1, columnspan = 1, padx = 2, pady = 10, ipadx = 5)

# Positive review keywords
poskw = Label(scrollable_frame, text = f'Top positive keywords:',
              font = 'Arial 15 bold', wraplength = 170, justify=CENTER)
poskw.grid(row = 10, column = 0, columnspan = 1, padx = 2, pady = 10)
poskw.config(foreground = 'blue')
posscor = Label(scrollable_frame, text = f'{summarystats.get_sum_poskw()}',
                font = 'Arial 15', wraplength = 200)
posscor.grid(row = 10, column = 1, columnspan = 1, padx = 2, pady = 10, ipadx = 5)

# Do better words
dobetter = Label(scrollable_frame, text = f'Improvable product attributes:',
                 wraplength = 200, font = 'Arial 15 bold', justify = CENTER)
dobetter.grid(row = 11, column = 0, columnspan = 2, padx = 2, pady = 10)
dobetter.config(foreground = 'blue')
dobetscor = Label(scrollable_frame, text = f'{summarystats.get_sum_dobet()}',
                  font = 'Arial 15', wraplength = 320)
dobetscor.grid(row = 12, column = 0, columnspan = 2, padx = 2, pady = 4)

# Quit button
quitbutton = Button(summwindow, height = 2, width = 5, text = "Quit", command = quit)
quitbutton.grid(row = 3, column = 0, columnspan = 2, pady = 8)


container.grid(column = 0, rowspan = 1, columnspan = 1, sticky = 'nw')
canvas.grid(column = 0, rowspan = 1, columnspan = 1, sticky = 'news')
scrollbar.grid(row = 0, column = 3, rowspan = 1, sticky = 'nsw')

summwindow.protocol("WM_DELETE_WINDOW", closing)

summwindow.mainloop()
