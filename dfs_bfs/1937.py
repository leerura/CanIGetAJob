import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solve():
    n = int(input().strip())

    trees = [list(map(int,input().split())) for _ in range(n)]

    #일단 최악의 방법으로 풀어보겠음
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    memo = [[-1]*n for _ in range(n)]

    def dfs(row,col):

        
        if(memo[row][col] !=-1):
            return memo[row][col]
        
        
        res = 1
        max_res = 0
        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]
            
            if(0<=nr<n and 0<=nc<n and trees[row][col] < trees[nr][nc]):
                max_res = max(max_res,dfs(nr,nc))
            
        res += max_res

        memo[row][col] = res
                

        return res
    
    answer =0
    
    
    for row in range(n):
        for col in range(n):
            answer = max(answer,dfs(row,col))
    
    print(answer)






if __name__ == "__main__":
    solve()