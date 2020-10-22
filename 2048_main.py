from tkinter import *

import constants as c
import logic
import random

class MainFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048 Game")
        self.master.bind("<Key>",self.key_down)
        
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
        Background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        Background.grid()

        for x in range(c.LEN):
            row_cells=[]
            for y in range(c.LEN):
                cur_cell=Frame(Background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.SIZE/c.LEN,height=c.SIZE/c.LEN)
                cur_cell.grid(row=x,column=y,padx=c.PADDING,pady=c.PADDING)
                
                cur_label= Label(master=cur_cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)
                cur_label.grid()
                row_cells.append(cur_label)
            self.grid_cells.append(row_cells)
        
    def Init_Matrix(self):
        self.matrix=logic.new_matrix()
        self.matrix_history=[]
        self.matrix=logic.add_2or4(self.matrix)
        self.matrix=logic.add_2or4(self.matrix)
        
    def Update_Cells(self):
        for x in range(c.LEN):
            for y in range(c.LEN):
                val=self.matrix[x][y]
                if val==0:
                    self.grid_cells[x][y].config(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[x][y].config(text=str(val),font=c.FONT,fg=c.CELL_COLOR_DICT[val],bg=c.BACKGROUND_COLOR_DICT[val])
        self.update_idletasks()
    
    def key_down(self,event):
        key=repr(event.char)
        if key==c.KEY_BACK and len(self.matrix_history)>=1:
            self.matrix=self.matrix_history.pop()
            self.Update_Cells()
            
            print("You are now on step %d." % len(self.matrix_history))
        elif key in self.commands:
            if self.matrix[0][0]==-1: return
            
            self.matrix_history.append(self.matrix)
            self.matrix=self.commands[key](self.matrix)
            self.matrix=logic.add_2or4(self.matrix)
            self.Update_Cells()
            
            Status=logic.check_status(self.matrix)
            if Status=="win":
                print("You Win!")
                self.matrix[0][0]=-1
                
                self.grid_cells[1][1].config(bg=c.BACKGROUND_COLOR_CELL_EMPTY,font=c.FONT,fg=c.FOREGROUND_COLOR_END,text="You")
                self.grid_cells[1][2].config(bg=c.BACKGROUND_COLOR_CELL_EMPTY,font=c.FONT,fg=c.FOREGROUND_COLOR_END,text="Win!")
            elif Status=="lose":
                print("You Lose!")
                self.matrix[0][0]=-1

                self.grid_cells[1][1].config(bg=c.BACKGROUND_COLOR_CELL_EMPTY,font=c.FONT,fg=c.FOREGROUND_COLOR_END,text="You")
                self.grid_cells[1][2].config(bg=c.BACKGROUND_COLOR_CELL_EMPTY,font=c.FONT,fg=c.FOREGROUND_COLOR_END,text="Lose!")
            elif Status=="continue":
                pass

if __name__=="__main__":
    start_game=MainFrame()