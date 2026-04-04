import sys

input = sys.stdin.readline

def solve():
    c,n = map(int,input().split())

    #메모리 낭비
    

    costs = []
    max_at_once = 0
    for _ in range(n):
        cost, customer = map(int, input().split())
        max_at_once = max(customer, max_at_once)
        costs.append((cost,customer))

    dp = [float('inf')] * (c+1+max_at_once)
    dp[0] = 0

    for i in range(1,c+1+max_at_once):
        for cost,customer in costs:
            if(i-customer>=0):
                dp[i] = min(dp[i],dp[i-customer]+ cost)

    answer = float('inf')
    for i in range(c,c+1+max_at_once):
        answer = min(answer,dp[i])

    print(answer)

if __name__=="__main__":
    solve()