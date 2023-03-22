import tkinter as tk

ROWS = 3
COLS = 3
PADDING = 5


class State():
    def __init__(self):
        self.state = [['e', 'e', 'e'],
                      ['e', 'e', 'e'],
                      ['e', 'e', 'e']]
        self.availableTiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def printState(self):
        for row in self.state:
            print(row)


class BoardVisual(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.columnconfigure(tuple(range(ROWS)), weight=1)
        self.rowconfigure(tuple(range(COLS)), weight=1)

        self.p1Turn = True

        # initialize buttons
        self.tiles = []
        i = 0
        for x in range(ROWS):
            for y in range(COLS):
                self.tiles.append(
                    tk.Button(self, font=('Arial', 30),  bg="white", borderwidth=1, command=lambda x=i: self.changeTileState(x)))
                self.tiles[i].grid(column=y, row=x, sticky="news")
                i += 1

    def updateGUI(self, state):
        pass

    def changeTileState(self, i):
        if self.tiles[i]['text'] != "X" and self.tiles[i]['text'] != "O" and self.p1Turn == True:
            self.tiles[i]['text'] = "X"
            self.p1Turn = False
        self.getCurrentState()

    def getCurrentState(self):
        CurrentState = State()
        for i, value in enumerate(self.tiles):
            print(i)
            CurrentState.state[i] = self.tiles[i]['text']
        CurrentState.printState()

    def resetBoard(self):
        pass


class InfoBar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#bbbbbb")

        self.columnconfigure(3, weight=1)
        self.rowconfigure(tuple(range(10)), weight=1)

        self.player1Score = "0"
        self.player2Score = "0"

        self.scoreLabel = tk.Label(self, text="Score", font=(
            'Arial', 18),  bg="#bbbbbb", borderwidth=1, padx=PADDING, pady=PADDING)
        self.scoreLabel.grid(row=30, column=1, sticky="EW")

        self.p1Scores = tk.Label(self, text="P1 " + self.player1Score, fg="blue", font=(
            'Arial', 18),  bg="#bbbbbb", borderwidth=1, padx=PADDING, pady=PADDING)
        self.p1Scores.grid(row=30, column=2, sticky="EW")

        self.p2Scores = tk.Label(self, text="P2 " + self.player2Score, fg="red", font=(
            'Arial', 18),  bg="#bbbbbb", borderwidth=1, padx=PADDING, pady=PADDING)
        self.p2Scores.grid(row=30, column=3, sticky="EW")


# initialize GUI=====================================
window = tk.Tk()
window.configure(bg="black")

infoBar = InfoBar(window)
infoBar.configure(width=30)
infoBar.pack(side="left", fill="both",
             padx=(PADDING, 0), pady=PADDING)

gameWindow = tk.Frame(window, bg="#eeeeee")
gameWindow.rowconfigure(0, weight=1)
gameWindow.columnconfigure(0, weight=1)
gameWindow.pack(side="right", fill="both", expand="true",
                padx=(PADDING, 0), pady=PADDING)

boardGUI = BoardVisual(gameWindow)
boardGUI.grid(row=0, column=0, sticky="news", padx=PADDING, pady=PADDING)

window.mainloop()
# ===================================================
