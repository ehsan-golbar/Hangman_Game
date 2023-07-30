from tkinter import *
entry_page = Tk()
entry_page.title("HangMan")
# entry page size and position
entry_page_height = 500
entry_page_weight = 500

screen_height  = entry_page.winfo_screenheight()
screen_weight =  entry_page.winfo_screenwidth()

entry_posx = screen_weight/2 - entry_page_weight/2
entry_posy = screen_height/2 - entry_page_height/2

entry_page.geometry("%dx%d+%d+%d" % (entry_page_weight, entry_page_height, entry_posx, entry_posy))





entry_page.mainloop()

