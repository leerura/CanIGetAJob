import sys

input = sys.stdin.readline

def solve():
    m, e, w, s, n = map(int, input().split())
    e= e/100
    w= w/100
    s= s/100
    n = n/100

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    prob = [e,w,s,n]

    visited = [[False] * (2*m+1) for _ in range(2*m+1)]

    total_prob = 0

    def dfs(row, col, probability,count):
        nonlocal total_prob
        if(count==m):
            total_prob += probability
            return
        
        visited[row][col] = True

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if(0<=nr<2*m+1 and 0<=nc<2*m+1 and not visited[nr][nc]):
                if prob[i] == 0: continue
                dfs(nr,nc,probability*prob[i],count+1)
        visited[row][col] = False

    dfs(m,m,1,0)


    
    print(total_prob)

if __name__=="__main__":
    solve()