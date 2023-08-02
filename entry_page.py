import tkinter.messagebox
from tkinter import *
from selected_word import selected_word
#from user_guess import user_guess_func


def user_guess_func( selected_word, chances) :
    global guess_word
    guess_word = " ".join("_" * len(selected_word))

    word_label = Label(game_frame, text=guess_word, font=("arial", 22))
    word_label.grid(row=0,column=0,pady= 20, columnspan=6, sticky="ew")
    alphabet_table.grid(row=1, column=0, columnspan=6)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ          "
    buttons = []
    counter = 0
    for row in range(1,6):
        for column in range(6):
            buttons.append(Button(alphabet_table, text=alphabet[counter], width=5, height=2,
                                  command=lambda i=alphabet[counter]: get_character(i)))
            buttons[counter].grid(row=row, column=column)
            counter += 1

    return True


def choose_level():
    level_frame.pack()
    registration_frame.pack_forget()
    Radiobutton(level_frame, text="Easy", variable=level_choice, value="easy").pack()
    Radiobutton(level_frame, text="Medium", variable=level_choice, value="medium").pack()
    Radiobutton(level_frame, text="Hard", variable=level_choice, value="hard").pack()
    Radiobutton(level_frame, text="Hardcore", variable=level_choice, value="hardcore").pack()
    Radiobutton(level_frame, text="Costume", variable=level_choice, value="costume").pack()
    pass_level_section_button = Button(level_frame, text="Next", command=start_game)
    pass_level_section_button.pack()


def start_game():
    global level_choice
    game_frame.pack()
    level_frame.pack_forget()
    easy, medium, hard = (False, False, False)
    chances = 6
    match level_choice:
        case "easy":
            easy = True
        case "medium":
            medium = True
            chances = 4
        case "hard":
            hard = True
            chances =2
        case "hardcore":
            easy, medium, hard = (True, True, True)
            chances = 2
        case "costum":
            easy = True  # later
    user_won = False

    while True:
        user_won = user_guess_func(selected_word(easy, medium, hard), chances)
        show_win_lose(user_won)
        flag = continue_game()
        if flag == "no":
            break


def show_win_lose(user_won):
    if user_won :
        tkinter.messagebox.showinfo(title="", message= "Well done, You Won!")
    else:
        tkinter.messagebox.showinfo(title="", message="sorry, you lost")


def continue_game():
    return tkinter.messagebox.askquestion("continue", "Do you want to continue the game ?")


def get_character(character):

    print(character)


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

# start game section
game_frame = Frame(entry_page)

# user guess
alphabet_table = Frame(game_frame)





entry_page.mainloop()

