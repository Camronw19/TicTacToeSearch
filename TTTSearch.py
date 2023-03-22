import tkinter as tk

ROWS = 3
COLS = 3


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
                    tk.Button(self, font=('Arial', 18),  bg="#eeeee4", borderwidth=1))
                self.tiles[i].grid(column=y, row=x, sticky="news")
                i += 1


window = tk.Tk()
boardGUI = BoardVisual(window)
boardGUI.pack()

window.mainloop()
