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
        registration_frame = tk.Frame(self)
        registration_frame.pack()
        welcom_lable = tk.Label(registration_frame, text="Welcome!")
        welcom_lable.pack()
        go_to_level_section = tk.Button(registration_frame, text="Next")
        go_to_level_section.pack()




        self.mainloop()






test = Hangman()