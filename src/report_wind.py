from tkinter import *
from tkinter import messagebox

reportwindow = Tk()

# Set sizes and placement of window
report_width = 410
report_height = 425
center_width = reportwindow.winfo_screenwidth()
center_height = reportwindow.winfo_screenheight()
center_x = int(center_width/2 - report_width / 2)
center_y = int(center_height/2 - report_height / 2)

reportwindow.geometry(f'{report_width}x{report_height}+{center_x}+{center_y}')
reportwindow.resizable(0, 0)
reportwindow.title('Amazon BI Product Report')

# Close menu function
def next():
    reportwindow.destroy()

# Closing protocol
def closing():
    if messagebox.askokcancel('Quit','Do you want to quit?'):
        sys.exit()

# Set labels
final_note = '  On a scoring scale from 1-10, with 10 being the most sellable'
final_score = 'Final product score:'
logist_score = 'Product attribute score:'
compet_score = 'Market competition\n score:'

titlelabel = Label(reportwindow, text = '\n' + prodchoice, font = ('Arial', 25, 'bold'))
titlelabel.grid(row = 1, column = 0, columnspan = 2, pady = 1)
titlelabel.config(foreground = 'purple')

analyslabel = Label(reportwindow, text = '\nSellable Product Analysis',
                    font = ('Arial', 18, 'bold'))
analyslabel.grid(row = 2, column = 0, columnspan = 2, pady = 1)

score_qlabel = Label(reportwindow, text = final_note, font = ('Arial', 14))
score_qlabel.grid(row = 3, column = 0, columnspan = 2, pady = 1)

fin_scorelabel = Label(reportwindow, text = final_score, font = ('Arial', 16))
fin_scorelabel.grid(row = 4, column = 0, columnspan = 2, pady = 1)

scoring_label = Label(reportwindow, text = overallscore.calculate_final_score(),
                      font = ('Arial', 40, 'bold'))
scoring_label.grid(row = 5, column = 0, columnspan = 2, pady = 1)

if overallscore.calculate_final_score() >= 9.0:
    scoring_label.config(foreground = 'blue')
if overallscore.calculate_final_score() >= 7.0 and overallscore.calculate_final_score() < 9.0:
    scoring_label.config(foreground = 'green')
if overallscore.calculate_final_score() >= 4.0 and overallscore.calculate_final_score() < 7.0:
    scoring_label.config(foreground = 'orange')
elif overallscore.calculate_final_score() >= 0.0 and overallscore.calculate_final_score() < 4.0:
    scoring_label.config(foreground = 'red')

logist_scorelabel = Label(reportwindow, text = '\n'+logist_score,
                          font = ('Arial', 16))
logist_scorelabel.grid(row = 6, column = 0, columnspan = 1, pady = 1)

logistscor_label = Label(reportwindow, text = overallscore.logist_cat_score(),
                         font = ('Arial', 25, 'bold'))
logistscor_label.grid(row = 7, column = 0, columnspan = 1, pady = 1)

if overallscore.logist_cat_score() >= 9.0:
    logistscor_label.config(foreground = 'blue')
if overallscore.logist_cat_score() >= 7.0 and overallscore.logist_cat_score() < 9.0:
    logistscor_label.config(foreground = 'green')
if overallscore.logist_cat_score() >= 4.0 and overallscore.logist_cat_score() < 7.0:
    logistscor_label.config(foreground = 'orange')
elif overallscore.logist_cat_score() >= 0.0 and overallscore.logist_cat_score() < 4.0:
    logistscor_label.config(foreground = 'red')


compet_scorelabel = Label(reportwindow, text = '\n'+compet_score, font = ('Arial', 16))
compet_scorelabel.grid(row = 6, column = 1, columnspan = 1, pady = 1)

competscor_label = Label(reportwindow, text = overallscore.comp_cat_score(),
                         font = ('Arial', 25, 'bold'))
competscor_label.grid(row = 7, column = 1, columnspan = 1, pady = 1)

if overallscore.comp_cat_score() >= 9.0:
    competscor_label.config(foreground = 'blue')
if overallscore.comp_cat_score() >= 7.0 and overallscore.comp_cat_score() < 9.0:
    competscor_label.config(foreground = 'green')
if overallscore.comp_cat_score() >= 4.0 and overallscore.comp_cat_score() < 7.0:
    competscor_label.config(foreground = 'orange')
elif overallscore.comp_cat_score() >= 0.0 and overallscore.comp_cat_score() < 4.0:
    competscor_label.config(foreground = 'red')
        
nextbutton = Button(reportwindow, height = 2, width = 18, text = "Summary Statistics",
                    command = next)
nextbutton.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10)

reportwindow.protocol("WM_DELETE_WINDOW", closing)

reportwindow.mainloop()
