from tkinter import *
# def set_level():
#     #test
#     lable = Label(entry_page, text=level_choice.get())
#     lable.pack()

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

# welcome lable
welcome_lable = Label(entry_page, text="Welcome to HangMan Game")
welcome_lable.pack()

# choosing level
level_frame = Frame(entry_page)
level_frame.pack()
level_choice = StringVar()
level_choice.set("easy")
Radiobutton(level_frame, text="Easy", variable=level_choice, value="easy", command=set_level).pack()
Radiobutton(level_frame, text="Medium", variable=level_choice, value="medium", command=set_level).pack()
Radiobutton(level_frame, text="Hard", variable=level_choice, value="hard", command=set_level).pack()
Radiobutton(level_frame, text="Hardcore", variable=level_choice, value="hardcore", command=set_level).pack()
Radiobutton(level_frame, text="Costume", variable=level_choice, value="costume", command=set_level).pack()





entry_page.mainloop()

