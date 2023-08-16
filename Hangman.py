import tkinter as tk


class Hangman(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman")

        window_height = 500
        window_width = 500
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        window_posx = screen_width / 2 - window_width / 2
        window_posy = screen_height / 2 - window_height / 2
        self.geometry("%dx%d+%d+%d" % (window_width, window_height, window_posx, window_posy))
        self.mainloop()






test = Hangman()