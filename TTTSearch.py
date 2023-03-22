import tkinter as tk

ROWS = 3
COLS = 3
PADDING = 5


class State():
    def __init__(self):
        self.state = [['e', 'e', 'e'],
                      ['e', 'e', 'e'],
                      ['e', 'e', 'e']]
        self.turn = 1
        self.availableTiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def printState(self):
        for row in self.state:
            print(row)


class BoardVisual(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(tuple(range(ROWS)), weight=1)
        self.rowconfigure(tuple(range(COLS)), weight=1)

        # initialize buttons
        self.tiles = []
        i = 0
        for x in range(ROWS):
            for y in range(COLS):
                self.tiles.append(
                    tk.Button(self, font=('Arial', 18),  bg="white", borderwidth=1))
                self.tiles[i].grid(column=y, row=x, sticky="news")
                i += 1


class InfoBar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#bbbbbb")

        self.columnconfigure(2, weight=1)
        self.rowconfigure(10, weight=1)

        self.scoreLabel = tk.Label(self, text="Score", font=(
            'Arial', 18),  bg="white", borderwidth=1, padx=PADDING, pady=PADDING)
        self.scoreLabel.grid(row=30, column=2, sticky="EW")


# main============

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
