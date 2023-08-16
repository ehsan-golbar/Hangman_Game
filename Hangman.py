import tkinter as tk


class Hangman(tk.Tk):
    def __init__(self):
        super().__init__()
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



        self.mainloop()


    def choose_level(self):
        self.level_frame.pack()
        self.registration_frame.pack_forget()


    def print_test(self):
        print(self.selected_level.get())

test = Hangman()