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

    for i in range(1,n):
        for w in range(16):
            for b in range(16):
                if(w+b-1>i):
                    continue
                res1 = dp[i-1][w][b]
                res2 = dp[i-1][w-1][b]+players[i][0] if w> 0 else -1
                res3 = dp[i-1][w][b-1]+players[i][1] if b>0 else -1
                dp[i][w][b] = max(res1,res2,res3)
    
    print(dp[n-1][15][15])

            
                
if __name__=="__main__":
    solve()