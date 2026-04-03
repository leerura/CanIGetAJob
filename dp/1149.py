import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    #"1번 집부터 i번 집까지 규칙을 지키며 칠했을 때, i번 집의 색이 color인 경우의 최소 비용"
    dp = [[0] *(3) for _ in range(n+1)] #r=0 g=1 b=2
    
    for i in range(1,n+1):
        prices = list(map(int, input().split()))

        for j in range(3):
            color1=0
            color2=0
            if(j==0):
                color1=1
                color2=2
            elif(j==1):
                color1 = 0
                color2 = 2
            else:
                color1 = 0
                color2 = 1

            dp[i][j] = min(dp[i-1][color1],dp[i-1][color2])+prices[j]


        
    answer = float('inf')
    for i in range(3):
        answer = min(answer,dp[n][i])
    print(answer)

        

if __name__=="__main__":
    solve()