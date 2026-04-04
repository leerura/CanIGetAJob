import sys

input = sys.stdin.readline

def solve():
    n,d = map(int,input().split())

    dp = [i for i in range(d+1)]
    

    cut = []

    for _ in range(n):
        s,e,c = map(int,input().split())
        if(e>d or c >= e-s): continue
        cut.append((s,e,c))


    for cur in range(1,d+1):
        dp[cur] = dp[cur-1] + 1
        for s,e,c in cut:
            if cur == e:
                dp[cur] = min(dp[s]+c,dp[cur])
                  
    print(dp[d])
 
if __name__=="__main__":
    solve()