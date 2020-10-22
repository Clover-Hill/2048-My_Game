import constants as c
import random

def new_matrix():
    matrix=[]
    for x in range(c.LEN):
        matrix.append([0]*c.LEN)
    return matrix

def add_2or4(matrix):
    full=True
    for row in range(c.LEN):
        for col in range(c.LEN):
            if matrix[row][col]==0: full= False
    if full: return matrix
    
    row=random.randint(0,c.LEN-1)
    col=random.randint(0,c.LEN-1)
    flag=random.randint(0,1)
    if flag: val=2
    else: val=4
    
    while matrix[row][col]!=0:
        row=random.randint(0,c.LEN-1)
        col=random.randint(0,c.LEN-1)
        
    matrix[row][col]=val
    return matrix

def merge(matrix):
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

def erase_space(matrix):
    for row in range(0,c.LEN):
        count=0
        for col in range(0,c.LEN):
            if matrix[row][col]!=0:
                matrix[row][count]=matrix[row][col]
                if count!=col: matrix[row][col]=0
                count+=1
    return matrix
    
def rotate(matrix):
    new_matrix=[]
    for row in range(0,c.LEN):
        new_row=[]
        for col in range(0,c.LEN):
            new_row.append(matrix[col][c.LEN-1-row])
        new_matrix.append(new_row)
    return new_matrix

def check_status(matrix):
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
def Left(matrix):
    matrix=merge(matrix)
    matrix=erase_space(matrix)
    
    return (matrix)
    
def Right(matrix):
    for i in range(0,2):
        matrix=rotate(matrix)
    matrix=Left(matrix)
    for i in range(0,2):
        matrix=rotate(matrix)
    return (matrix)

def Up(matrix):
    for i in range(0,1):
        matrix=rotate(matrix)
    matrix=Left(matrix)
    for i in range(0,3):
        matrix=rotate(matrix)
    return (matrix)
    
def Down(matrix):
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