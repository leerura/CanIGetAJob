import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    prices = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)] #i<=j 

    for length in range(1,n+1):
        for i in range(n-length):
            max_value = 0
            for k in range(i,i+length):
                left_part = sum(prices[i:k])-dp[i][k-1] if(k>i) else 0
                right_part = sum(prices[k+1:i+length]) - dp[k+1][i+length-1] if k<i+length-1 else 0
                current_val = prices[k] + left_part + right_part
                max_value = max(max_value,current_val)

            dp[i][i+length-1] = max_value

    print(dp)







    #dp[i][j] #i번 기타부터 j번 기타까지 연속된 하나의 그룹이 남았을 때, 현재 차례인 사람이 이 그룹에서 얻을 수 있는 가치의 최대 합.



