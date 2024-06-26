from tkinter import messagebox
from highscore import get_highscore, set_highscore

class game:
    def __init__(self, gamepanel, return_callback):
        self.gamepanel = gamepanel
        self.return_callback = return_callback
        self.end = False
        self.won = False

    def start(self):
        self.reset()
        self.gamepanel.window.mainloop()
    
    def reset(self):
        self.end = False
        self.won = False
        self.gamepanel.reset()
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.keys)

    def keys(self, event):
        presed_key = event.keysym

        if presed_key == 'Up':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif presed_key == 'Down':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif presed_key == 'Left':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif presed_key == 'Right':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()

        else:
            pass

        self.gamepanel.paintGrid()
        
        flag = 0
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j] == 2048:
                    flag = 1
                    break

        if flag == 1:
            self.won = True
            messagebox.showinfo('2048', message='Вы выиграли!\nВаш счёт: ' + str(self.gamepanel.score))

            if self.gamepanel.score > get_highscore():
                set_highscore(self.gamepanel.score)

            self.return_to_main_menu()
            return

        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j] == 0:
                    flag = 1
                    break

        if not (flag or self.gamepanel.can_merge()):
            self.end = True
            messagebox.showinfo('2048', 'Вы проиграли...\nВаш счёт: ' + str(self.gamepanel.score))

            if self.gamepanel.score > get_highscore():
                set_highscore(self.gamepanel.score)

            self.return_to_main_menu()
            return

        if self.gamepanel.moved:
            self.gamepanel.random_cell()

        self.gamepanel.paintGrid()

    def return_to_main_menu(self):
        self.gamepanel.window.destroy()
        self.return_callback()
