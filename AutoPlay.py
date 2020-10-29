from MainFrame import *
from copy import deepcopy
import constants as c
import queue

class AutoPlay(MainFrame):
    def __init__(self):
        MainFrame.__init__(self)
        self.max_queue_size = 500
        
        self.que=queue.Queue()
        self.que.put(self.matrix)
        
        self.trace_step=list()
        self.trace_step.append([-1,self.matrix,-1])
        
        self.solve()
        self.show_ans()
        
        if __name__ == '__main__':
            self.mainloop()
        
    def solve(self):
        step=-1
        while not self.que.empty():
            cur_matrix=deepcopy(self.que.get())
            four_dir_que=queue.PriorityQueue()
            
            if step==1000000: break
            if logic.check_status(cur_matrix)=="win":
                break
            
            for name,cur_dir in self.commands.items():
                nxt_matrix=cur_dir(cur_matrix)
                nxt_matrix=logic.add_2or4(nxt_matrix)
                
                if logic.check_status(nxt_matrix)=="lose" or nxt_matrix==cur_matrix:
                    continue
                    
                four_dir_que.put([-1*self.get_val(nxt_matrix),nxt_matrix,name])
            
            step=step+1
            while not four_dir_que.empty():
                cur_dir=four_dir_que.get()
                if self.que.qsize()>self.max_queue_size:
                    break
                
                self.que.put(cur_dir[1])
                self.trace_step.append([step,cur_dir[1],cur_dir[2]])

    def get_val(self,matrix):
        ret=0
        ret+=self.floor_like(matrix)*2
        ret+=self.blank_space_num(matrix)*256
        ret+=self.max_num(matrix)*8
        return ret
        
    def floor_like(self,matrix):
        ret=0
        for k in range(c.LEN-1):
            if matrix[0][k] and matrix[0][k+1] :
                ret=ret+matrix[0][k+1]-matrix[0][k]
            if matrix[2][k] and matrix[2][k+1] :
                ret=ret+matrix[2][k+1]-matrix[2][k]
                
        for k in range(c.LEN-1,0,-1):
            if matrix[1][k] and matrix[1][k-1] :
                ret=ret+matrix[1][k-1]-matrix[1][k]
            if matrix[3][k] and matrix[3][k-1] :
                ret=ret+2*(matrix[3][k-1]-matrix[3][k])
        return ret
        
    def blank_space_num(self,matrix):
        ret=0
        for x in range(c.LEN):
            for y in range(c.LEN):
                if matrix[x][y]==0:
                    ret+=1
        return ret
        
    def max_num(self,matrix):
        ret=0
        for x in range(c.LEN):
            for y in range(c.LEN):
                ret=max(ret,matrix[x][y])
        return ret
        
    def show_ans(self):
        ans_stack=queue.LifoQueue()
        cur_num=len(self.trace_step)-1

        while self.trace_step[cur_num][0]!=-1:
            ans_stack.put([ self.trace_step[cur_num][1] , self.trace_step[cur_num][2]])
            cur_num=self.trace_step[cur_num][0]
            
            # print(cur_num)
            # print(self.trace_step[cur_num][2])
            
        while not ans_stack.empty():
            tmp_matrix=ans_stack.get()
            
            print(tmp_matrix[1])
            if tmp_matrix[1]=="'w'":
                self.after(1500,self.event_generate('w'))
            elif tmp_matrix[1]=="'s'":
                self.after(1500,self.event_generate('s'))
            elif tmp_matrix[1]=="'d'":
                self.after(1500,self.event_generate('d'))
            elif tmp_matrix[1]=="'a'":
                self.after(1500,self.event_generate('a'))
            else: raise ValueError
        
start_game=AutoPlay()