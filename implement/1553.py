import sys

input = sys.stdin.readline

def solve():
    data =[[] for _ in range(8)]
    for i in range(8):
        line = input().strip()
        for num in line:
            data[i].append(int(num))
    
    visited = [[False] * 7 for _ in range(8)]
    used_domino = [[False] * 7 for _ in range(7)]

    def dfs(row,col):
        if(row==8):
            return 1
        next_row, next_col = (row,col+1) if(col+1 <=6) else (row+1,0)

        if(visited[row][col]):
            return dfs(next_row,next_col)
        
        res = 0 #어짜피 1 or 0임
        visited[row][col]=True
        cur = data[row][col]
        #가로로 놓기
        if(col+1<=6 and not visited[row][col+1]):
            next = data[row][col+1]
            if(not used_domino[min(cur,next)][max(cur,next)]):
                visited[row][col+1] = True
                used_domino[min(cur,next)][max(cur,next)] = True
                res += dfs(next_row,next_col)
                visited[row][col+1] = False
                used_domino[min(cur,next)][max(cur,next)] = False

        if(row+1<=7 and not visited[row+1][col]):
            next = data[row+1][col]
            if(not used_domino[min(cur,next)][max(cur,next)]):
                visited[row+1][col] = True
                used_domino[min(cur,next)][max(cur,next)] = True
                res += dfs(next_row,next_col)
                visited[row+1][col] = False
                used_domino[min(cur,next)][max(cur,next)] = False
        visited[row][col]=False


        return res

    print(dfs(0,0))



if __name__=="__main__":
    solve()