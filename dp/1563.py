import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    #dp[day][late][absent] 특정 day에 총 특정 번 late하고 연속 absent인 수
    dp = [[[0] * 3 for _ in range(2)] for __ in range(n+1) ]

    dp[0][0][0] = 1

    for d in range(n):
        for l in range(2):
            for a in range(3):
                if (dp[d][l][a] == 0):
                    continue

                cur = dp[d][l][a]

                dp[d+1][l][0] = (dp[d+1][l][0] + cur)%1000000

                if(l==0):
                    dp[d+1][l+1][0] = (dp[d+1][l+1][0] + cur)%1000000

                if(a<2):
                    dp[d+1][l][a+1] = (dp[d+1][l][a+1] + cur)%1000000

    answer = 0
    for l in range(2):
        for a in range(3):
            answer += dp[n][l][a]
    print(answer)


if __name__ =="__main__":
    solve()