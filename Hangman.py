import tkinter as tk


class Hangman(tk.Tk):
    def __init__(self):
        super().__init__()
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
        go_to_level_section = tk.Button(self.registration_frame, text="Next", command= self.choose_level)
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
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ          "
        buttons = []
        counter = 0
        for row in range(1, 6):
            for column in range(6):
                buttons.append( tk.Button(self.letters_table, text= letters[counter], width=5, height=2,
                                          command=lambda i=letters[counter], index = counter : self.get_character(i, index) ))
                buttons[counter].grid(row=row, column=column)
                counter += 1


        self.mainloop()


    def choose_level(self):
        self.level_frame.pack()
        self.registration_frame.pack_forget()


    def start_game(self):
        self.game_section.pack()
        self.letters_table.grid(row=1, column=0, columnspan=6)
        self.level_frame.pack_forget()
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
        print((easy, medium, hard))
        self.selecte_word(easy, medium, hard)

    def get_character(self, character, index):
        pass

    def selecte_word(self, easy, medium, hard):
        self.selected_word = "salam"
        print(self.selected_word)

    def print_test(self):
        print(self.selected_level.get())

test = Hangman()