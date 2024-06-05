from tkinter import Tk, Frame, Label
from highscore import get_highscore, set_highscore
from random import choice

class board:
    bg_color = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#ecd27e',
        '16': '#eccc61',
        '32': '#efab9b',
        '64': '#f48c74',
        '128': '#ef8dde',
        '256': '#f28cea',
        '512': '#e3b5f8',
        '1024': '#ca78e8',
        '2048': '#adcfff',
    }
    color = {
        '2': '#f9f6f2',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.n = 4
        self.window = Tk()

        self.window.title('2048 Game')
        self.gameArea = Frame(self.window, bg='azure3')
        self.gameArea.grid(row=0, column=0)

        self.board = []
        self.gridCell = [[0]*4, [0]*4, [0]*4, [0]*4]

        self.compress = False
        self.merge = False
        self.moved = False

        self.score = 0

        for i in range(4):
            rows = []
            for j in range(4):
                l = Label(self.gameArea, text='', bg='azure4',
                font = ('arial',22,'bold'), width=4, height=2)
                l.grid(row=i, column=j, padx=10, pady=10)

                rows.append(l)
            self.board.append(rows)

        self.window.after(100, self.center_window)
        self.window.resizable(False, False)

    def center_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    def reset(self):
        if self.score > get_highscore():
            set_highscore(self.score)
    
        self.gridCell = [[0]*4, [0]*4, [0]*4, [0]*4]
        self.score = 0

    def reverse(self):
        for ind in range(4):
            i = 0
            j = 3
            while i < j:
                self.gridCell[ind][i],self.gridCell[ind][j] = self.gridCell[ind][j],self.gridCell[ind][i]
                i += 1
                j -= 1

    def transpose(self):
        self.gridCell = [list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress = False
        temp = [[0]*4, [0]*4, [0]*4, [0]*4]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt] = self.gridCell[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def mergeGrid(self):
        self.merge = False
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells = []
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr = choice(cells)
        i = curr[0]
        j = curr[1]
        self.gridCell[i][j] = 2

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    self.board[i][j].config(text='', bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))