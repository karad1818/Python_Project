class create_env:
    def __init__(self):
        self.matrix = [['-' , '-' , '-'] ,
                       ['-' , '-' , '-'],
                       ['-' , '-' , '-']
                      ]
        
    def get_element(self , row , col):
        return self.matrix[row-1][col-1]
    
    def update(self,row,col,mark):
        self.matrix[row-1][col-1] = mark
    
    def is_full(self):
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt += (self.matrix[i][j] == '-')
        return cnt == 0
    
    def print_board(self):
        s = ""
        for i in range(3):
            for j in range(3):
                s += f"|{self.matrix[i][j]}"
            s += "|\n"
        print(s)

    
class minimax:
    def __init__(self , matrix):
        self.matrix = matrix
        self.row = -1
        self.col = -1
    
    def is_full(self):
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt += (self.matrix[i][j] == '-')
        return cnt == 0
    
    def reward(self):
        # row checker
        for i in range(3):
            sc1 , sc2 = 0 , 0
            for j in range(3):
                sc1 += (self.matrix[i][j] == 'O')
                sc2 += (self.matrix[i][j] == '+')
            if sc1 == 3:
                return 1
            if sc2 == 3:
                return -1
            
        # col checker
        for i in range(3):
            sc1 , sc2 = 0 , 0
            for j in range(3):
                sc1 += (self.matrix[j][i] == 'O')
                sc2 += (self.matrix[j][i] == '+')
            if sc1 == 3:
                return 1
            if sc2 == 3:
                return -1
            
        # diagonal1 checker
        sc1 , sc2 = 0 , 0
        for i in range(3):
            sc1 += (self.matrix[i][i] == 'O')
            sc2 += (self.matrix[i][i] == '+')
        if sc1 == 3:
            return 1
        if sc2 == 3:
            return -1
        
        # diagonal2 checker
        sc1 , sc2 = 0 , 0 
        for i in range(3):
            sc1 += (self.matrix[i][(2-i)] == 'O')
            sc2 += (self.matrix[i][(2-i)] == '+')
        if sc1 == 3:
            return 1
        if sc2 == 3:
            return -1
        return 0
        
    def get_row_col(self , mx):
        if mx == True:
            best = [-1000 , -1 , -1]
        else:
            best = [1000 , -1 , -1]

        if self.is_full() == True or self.reward() == -1 or self.reward() == 1:
            return [self.reward() , -1 , -1 ] 
        
        if mx == True:
            for i in range(3):
                for j in range(3):
                    if self.matrix[i][j] == '-':
                        self.matrix[i][j] = 'O'
                        score = self.get_row_col(False)
                        self.matrix[i][j] = '-'
                        score[1] , score[2] = i+1 , j+1
                        if score[0] > best[0] :
                            best = score
            return best
                        
        if mx == False:
            score = 1000000
            for i in range(3):
                for j in range(3):
                    if self.matrix[i][j] == '-':
                        self.matrix[i][j] = '+'
                        score = self.get_row_col(True)
                        self.matrix[i][j] = '-'
                        score[1] , score[2] = i+1 , j+1
                        if score[0] < best[0] :
                            best = score
            return best
            
    
if __name__ == '__main__':
    env = create_env()
    
    print("Do you want first turn [y/n] : ")
    t = str(input())

    turn = True
    if t == 'y':
        turn = False
    
    msg = False
    while env.is_full() == False:
        if turn == False:
            print("Give your input[row_no col_no] : ")
            st = str(input())
            row , col = int(st[0]) , int(st[2])
            env.update(row , col , '+')
            env.print_board()
            turn = True
        else:
            A = minimax(env.matrix)
            best = A.get_row_col(True)
            env.update(best[1] , best[2] , 'O')
            turn = False
            env.print_board()

            if A.reward() == 1:
                print("You Loose ) :")
                msg = True
                break
            if A.reward() == -1:
                print("You won : )")
                msg = True
                break
    if msg == False:
        print("Draw :))")