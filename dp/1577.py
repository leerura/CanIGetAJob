import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    k = int(input().strip())

    dp = [[0] * (m+1) for _ in range(n+1)] #dp[x][y]
    dp[0][0] = 1

    roads = set()

    for _ in range(k):
        a,b,c,d = map(int, input().split())
        roads.add((a,b,c,d)) 
    
    

    
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 and j==0):
                continue
            left = dp[i-1][j] if i-1>=0 else 0
            if((i,j,i-1,j) in roads or (i-1,j,i,j) in roads):
                left = 0
            

            down = dp[i][j-1] if j-1>=0 else 0
            if ((i,j,i,j-1) in roads or (i,j-1,i,j) in roads):
                down = 0

            dp[i][j] = left+down


    print(dp[n][m])


if __name__=="__main__":
    solve()