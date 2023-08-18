import tkinter as tk
import tkinter.messagebox as tkm

from PIL import ImageTk, Image
from rembg import remove

class Hangman(tk.Tk):
    def __init__(self):
        super().__init__()
        self.guess_word = ""
        self.selected_word = ""
        self.chances = 6
        self.title("Hangman")
        # put the window in center of screen
        window_height = 500
        window_width = 500
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        window_posx = screen_width / 2 - window_width / 2
        window_posy = screen_height / 2 - window_height / 2
        self.geometry("%dx%d+%d+%d" % (window_width, window_height, window_posx, window_posy))
        # registration section
        self.registration_frame = tk.Frame(self)
        self.registration_frame.pack()
        welcom_lable = tk.Label(self.registration_frame, text="Welcome!")
        welcom_lable.pack()
        next_photo = ImageTk.PhotoImage( remove(Image.open('pic/next.png')).resize((90,60)))

        go_to_level_section = tk.Button(self.registration_frame, image= next_photo , borderwidth= 0 , command= self.choose_level)
        go_to_level_section.size()
        go_to_level_section.pack()
        # level section
        self.level_frame = tk.Frame(self)
        self.selected_level = tk.StringVar()
        self.selected_level.set("easy")
        tk.Radiobutton(self.level_frame, text="Easy", variable= self.selected_level, value="easy").pack()
        tk.Radiobutton(self.level_frame, text="Medium", variable=self.selected_level, value="medium").pack()
        tk.Radiobutton(self.level_frame, text="Hard", variable= self.selected_level, value="hard").pack()
        tk.Radiobutton(self.level_frame, text="Hardcore", variable= self.selected_level, value="hardcore").pack()
        tk.Radiobutton(self.level_frame, text="Costume", variable= self.selected_level, value="costume").pack()
        go_to_game = tk.Button(self.level_frame, text="Next", command= self.start_game).pack()
        # start_game section
        self.game_section = tk.Frame(self)
        self.letters_table = tk.Frame(self.game_section)
        self.letters_table.grid(row=1, column=0, columnspan=6)
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ          "
        buttons = []
        counter = 0
        for row in range(1, 6):
            for column in range(6):
                if letters[counter] == " ":
                    break
                buttons.append( tk.Button(self.letters_table, text= letters[counter], width=5, height=2,
                                          command=lambda i=letters[counter], index = counter : self.get_character(i, index) ))
                buttons[counter].grid(row=row, column=column)
                counter += 1
        buttons[25].grid(column= 3)
        buttons[24].grid(column= 2)
        self.guess_word_lable = tk.Label(self.game_section, text= self.guess_word, font=("arial", 22))
        self.guess_word_lable.grid(row= 0, column= 0, columnspan= 6, sticky="ew", pady=20)
        self.chances_lable = tk.Label(self.game_section,  text="chances : " + str(self.chances) )
        self.chances_lable.grid(row= 6, column = 0)

        self.mainloop()


    def choose_level(self):
        self.level_frame.pack()
        self.registration_frame.pack_forget()


    def start_game(self):
        easy, medium, hard = (False, False, False)
        match self.selected_level.get():
            case "easy":
                easy = True
            case "medium":
                medium = True
                self.chances = 4
            case "hard":
                hard = True
                self.chances = 2
            case "hardcore":
                easy, medium, hard = (True, True, True)
                self.chances = 2
            case "costume":
                easy = True  # later
        #print((easy, medium, hard))
        self.selecte_word(easy, medium, hard)
        self.guess_word = " ".join("_"*len(self.selected_word))
        #print(self.guess_word)
        self.guess_word_lable.config(text=self.guess_word)
        self.chances_lable.config(text="chances : " + str(self.chances) )
        self.game_section.pack()
        self.level_frame.pack_forget()

    def get_character(self, character, index):
        if character in self.selected_word :
            self.guess_word = " ".join([c if c == character or c in self.guess_word else "_" for c in self.selected_word])
            self.guess_word_lable.config(text=self.guess_word)
        else:
            self.chances -= 1
            self.chances_lable.config(text="chances : " + str(self.chances))

        self.check_win_or_lose()


    def check_win_or_lose(self):
        if "_" in self.guess_word :
            if self.chances == 0 :
                tkm.showinfo(title="", message="sorry, you lost")
                self.continue_game()
        else:
            tkm.showinfo(title="", message="Well done, You Won!")
            self.continue_game()
    def selecte_word(self, easy, medium, hard):
        self.selected_word = "SALAM"
       # print(self.selected_word)

    def continue_game (self):
        continue_flag = tkm.askquestion("continue?", " Do you want to try again ?")
        if continue_flag == "yes":
            self.game_section.pack_forget()
            self.choose_level()
        else :
            self.quit()
    def print_test(self):
        print(self.selected_level.get())
test = Hangman()