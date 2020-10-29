import constants as c
import random
from copy import deepcopy

def new_matrix():
    matrix=[]
    for x in range(c.LEN):
        matrix.append([0]*c.LEN)
    return matrix

def add_2or4(_matrix):
    matrix=deepcopy(_matrix)

    full=True
    for row in range(c.LEN):
        for col in range(c.LEN):
            if matrix[row][col]==0: full= False
    if full: return matrix
    
    flag=random.randint(0,1)
    if flag: val=2
    else: val=4
    
    empty_cells=list()
    for x in range(c.LEN):
        for y in range(c.LEN):
            if matrix[x][y]==0:
                empty_cells.append([x,y])
    row,col=empty_cells[random.randint(0,len(empty_cells)-1)]
    matrix[row][col]=val
    return matrix

def merge(_matrix):
    matrix=deepcopy(_matrix)

    for row in range(0,c.LEN):
        lst_pos=c.LEN
        lst_val=-100

        for col in range(0,c.LEN):
            cur_val=matrix[row][col]
            if cur_val==0: continue
            
            if lst_pos==c.LEN:
                lst_pos=col
                lst_val=cur_val
                continue
            
            if cur_val==lst_val:
                matrix[row][col]*=2
                matrix[row][lst_pos]=0
                lst_pos=c.LEN
                lst_val=-100
            else:
                lst_pos=col
                lst_val=matrix[row][col]
    return matrix

def erase_space(_matrix):
    matrix=deepcopy(_matrix)

    for row in range(0,c.LEN):
        count=0
        for col in range(0,c.LEN):
            if matrix[row][col]!=0:
                matrix[row][count]=matrix[row][col]
                if count!=col: matrix[row][col]=0
                count+=1
    return matrix
    
def rotate(_matrix):
    matrix=deepcopy(_matrix)

    new_matrix=[]
    for row in range(0,c.LEN):
        new_row=[]
        for col in range(0,c.LEN):
            new_row.append(matrix[col][c.LEN-1-row])
        new_matrix.append(new_row)
    return new_matrix

def check_status(_matrix):
    matrix=deepcopy(_matrix)

    win=False
    lose=True
    
    for row in range(0,c.LEN):
        for col in range(0,c.LEN):
            if matrix[row][col]==2048:
                win=True
            if matrix[row][col]==0:
                lose=False
    if win: return "win"
    if not lose: return "continue"
    
    lose=True
    for row in range(0,c.LEN):
        for col in range(0,c.LEN-1):
            if matrix[row][col]==matrix[row][col+1] or matrix[col][row]==matrix[col+1][row]:
                lose=False
    if not lose: return "continue"
    else: return "lose"

#movement Commands return (Status , matrix)
def Left(_matrix):
    matrix=deepcopy(_matrix)

    matrix=merge(matrix)
    matrix=erase_space(matrix)
    
    return (matrix)
    
def Right(_matrix):
    matrix=deepcopy(_matrix)

    for i in range(0,2):
        matrix=rotate(matrix)
    matrix=Left(matrix)
    for i in range(0,2):
        matrix=rotate(matrix)
    return (matrix)

def Up(_matrix):
    matrix=deepcopy(_matrix)

    for i in range(0,1):
        matrix=rotate(matrix)
    matrix=Left(matrix)
    for i in range(0,3):
        matrix=rotate(matrix)
    return (matrix)
    
def Down(_matrix):
    matrix=deepcopy(_matrix)

    for i in range(0,3):
        matrix=rotate(matrix)
    matrix=Left(matrix)
    for i in range(0,1):
        matrix=rotate(matrix)
    return (matrix)

if __name__ == "__main__":
    Matrix=[
        [256,128,128,4],
        [2,4,16,8],
        [4,8,4,2],
        [8,2,16,8]
        ]
    
    print(check_status(Matrix))
    Matrix=merge(Matrix)
    for row in range(0,c.LEN):
        for col in range(0,c.LEN):
            print(Matrix[row][col],end=" ")
        print()