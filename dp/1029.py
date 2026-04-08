import sys

imput = sys.stdin.readline

def solve():
    n = int(input().strip())

    prices = [input().strip() for _ in range(n)] # index => +1 해야됨
    visited = [False] * n


    def dfs(artist,get):
        res = 1
        visited[artist] = True

        max_value = 0
        for j in range(n):
            if artist==j: continue
            next = int(prices[artist][j])
            if(get <= next and not visited[j]):
                max_value = max(max_value,dfs(j,next))


        visited[artist] = False

        return res+max_value

    print(dfs(0,0))

    """

    dp = [(-1,-1)] * n # i가 소유했을 때 (최대 횟수, 산가격)

    dp[0] = (1,0)
    




    for i in range(n):
        if dp[i][0] == -1:
            continue

        count, price = dp[i]

        for j in range(n):
            if(i==j): continue

            if(int(prices[i][j])>= price and count+1 > dp[j][0]):
                dp[j] = (count+1,int(prices[i][j]))
                


    print(dp)
    """






if __name__=="__main__":
    solve()
