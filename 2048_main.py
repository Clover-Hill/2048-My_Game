from tkinter import *

import constants as c
import logic

class MainFrame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("2048 Game")
        self.master.bind("<key>",key_down)
        
        self.commands={
            c.KEY_DOWN: logic.Down,
            c.KEY_UP: logic.Up,
            c.KEY_LEFT: logic.Left,
            c.KEY_RIGHT: logic.Right,

            c.KEY_DOWN_ALT: logic.Down,
            c.KEY_UP_ALT: logic.Up,
            c.KEY_LEFT_ALT: logic.Left,
            c.KEY_RIGHT_ALT: logic.Right,
        }
        
        self.grid_cells=[]
        self.matrix=[]
        
        self.Init_Grid()
        self.Init_Matrix()
        self.Update_Cells()

        self.mainloop()

    def Init_Grid(self):
        for x in range(c.LEN):
            row_cells=[]
            for y in range(c.LEN):
                cur_Grid=Frame(self,bg=c.CELL_BACKGROUND_COLOR,width=c.WIDTH/c.LEN,height=c.HEIGHT/c.LEN)
                cur_Grid.grid(row=x,col=y,padx=c.CELL_PAD,pady=c.CELL_PAD)
                row_cells.append(cur_Grid)
            self.grid_cells.append(row_cells)
        
    def Init_Matrix(self):
        for x in range(c.LEN):
            self.matrix.append([0]*c.LEN)
        self.matrix_history=[]
        self.matrix=logic.add_2or4(self.matrix)
        self.matrix=logic.add_2or4(self.matrix)
        
    def Update_Cells(self):
        for x in range(c.LEN):
            for y in range(c.LEN):
                val=self.matrix[x][y]
                if val==0:
                    num_label=Label(self.grid_cells[x][y],text="",font=c.FONT,fg=c.NUM_COLOR_DICT[val])
                else:
                    num_lael=Label(self.grid_cells[x][y],text=str(val),font=c.FONT,fg)
    
        
    
