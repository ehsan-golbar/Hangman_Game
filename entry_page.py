from tkinter import *
# def set_level():
#     #test
#     lable = Label(level_frame, text=level_choice.get())
#     lable.pack()
def choose_level():
    level_frame.pack()
    registration_frame.pack_forget()


def start_game():
    game_frame.pack()
    level_frame.pack_forget()
    Label(game_frame, text="salam").pack()


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

# registreation section
registration_frame = Frame(entry_page)
registration_frame.pack()
welcome_lable = Label(registration_frame, text="Welcome to HangMan Game")
welcome_lable.pack()





pass_registration_section_button = Button(registration_frame, text="Next", command=choose_level)

pass_registration_section_button.pack()

# choosing level
level_frame = Frame(entry_page)

level_choice = StringVar()
level_choice.set("easy")
Radiobutton(level_frame, text="Easy", variable=level_choice, value="easy").pack()
Radiobutton(level_frame, text="Medium", variable=level_choice, value="medium").pack()
Radiobutton(level_frame, text="Hard", variable=level_choice, value="hard").pack()
Radiobutton(level_frame, text="Hardcore", variable=level_choice, value="hardcore").pack()
Radiobutton(level_frame, text="Costume", variable=level_choice, value="costume").pack()
pass_level_section_button = Button(level_frame, text= "Next", command= start_game)
pass_level_section_button.pack()

# start game section
game_frame = Frame(entry_page)







entry_page.mainloop()

