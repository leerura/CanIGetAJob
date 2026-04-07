import sys

input = sys.stdin.readline

def solve():

    players = []

    for line in sys.stdin:
        line = line.strip()    
        if not line: # 빈 줄이면 건너뜀
            continue
        w, b = map(int, line.split())
        players.append((w,b))

    n = len(players) #player idx 0~n-1

    dp =[[[-1] * 16 for _ in range(16)] for __ in range(n)] #dp[i][w][b]

    dp[0][0][0] = 0
    dp[0][1][0] = players[0][0]
    dp[0][0][1] = players[0][1]

    for i in range(n):
       
        for w in range(16):
            for b in range(16):
                if(dp[i][w][b] == -1 or w+b-1>i):
                    continue
                
                if(i+1<=n-1):
                    dp[i+1][w][b] = max(dp[i+1][w][b],dp[i][w][b])

                if(i+1<=n-1 and w+1 <=15):
                    dp[i+1][w+1][b] = max(dp[i+1][w+1][b],dp[i][w][b]+players[i+1][0])

                if(i+1<=n-1 and b+1 <=15):
                    dp[i+1][w][b+1] = max(dp[i+1][w][b+1],dp[i][w][b]+players[i+1][1])

    print(dp[n-1][15][15])


if __name__=="__main__":
    solve()


    