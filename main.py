from tkinter import Tk, Button, Label, Frame
from game_logic import game
from board import board
from tkvideo import tkvideo
from highscore import get_highscore

class StartMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title('2048')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width // 2) - (500 // 2)
        y = (screen_height // 2) - (500 // 2)
        self.window.geometry(f'500x500+{x}+{y}')

        self.video_frame = Frame(self.window, width=500, height=500)
        self.video_frame.pack()
        self.video_label = Label(self.video_frame)
        self.video_label.pack()
        self.video_player = tkvideo('files/bgvideo.mp4', self.video_label, loop=1, size=(500, 500))
        self.video_player.play()

        title_label = Label(self.window, text='2048', font=('arial', 30, 'bold'))
        title_label.place(relx=0.5, rely=0.2, anchor='center')

        high_score = get_highscore()

        high_score_label = Label(self.window, text=f'Рекорд: {high_score}', font=('arial', 14))
        high_score_label.place(relx=0.5, rely=0.3, anchor='center')

        start_button = Button(self.window, text='Старт', command=self.start_game, font=('arial', 14))
        start_button.place(relx=0.5, rely=0.5, anchor='center')

        quit_button = Button(self.window, text='Выход', command=self.window.quit, font=('arial', 14))
        quit_button.place(relx=0.5, rely=0.7, anchor='center')

        self.window.mainloop()
    
    def start_game(self):
        self.window.destroy()
        game_panel = board()
        game_instance = game(game_panel, StartMenu)
        game_instance.start()

if __name__ == '__main__':
    StartMenu()