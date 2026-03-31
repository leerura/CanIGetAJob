import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solve():
    n,m = map(int,input().split()) #n = row, m =col
    matrix = [[0] * m for _ in range(n)]

    data = []

    for _ in range(n):
        data.append(input().strip())

    for row in range(n):
        for col in range(m):
            matrix[row][col] = data[row][col]

    answer = 0

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    has_answer = True

    visited = [[False] * m for _ in range(n)]
    memo = [[-1]*m for _ in range(n)]


    def dfs(row,col):
        nonlocal answer
        nonlocal has_answer

        if(visited[row][col]):
            has_answer = False
            return 0
        
        if memo[row][col] != -1:
            return memo[row][col]
        
        if(matrix[row][col] == "H"):
            return 0
        
        visited[row][col] = True
        
        x = int(matrix[row][col])

        max_dist = 0

        for i in range(4):
            nr = row +dr[i]*x
            nc = col +dc[i]*x
            
            if(0<=nr<n and 0<=nc<m):
                res = dfs(nr,nc) 
                if not has_answer: return 0 #전파 대박이네
                max_dist = max(max_dist,res+1)
            else:
                max_dist = max(max_dist,1)

                

        visited[row][col] = False
        memo[row][col] = max_dist
        return max_dist
    

    dfs(0,0)

    if(has_answer):
        print(memo[0][0])
    else:
        print(-1)
        

if __name__ == "__main__":
    solve()