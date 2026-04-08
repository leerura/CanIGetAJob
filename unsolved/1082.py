import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    prices = list(map(int,input().split()))
    m = int(input().strip())

    dp = ["-1"] * (m+1) #dp[i] = i원으로 만들 수 있는 최대 수

    for i in range(n):
        price = prices[i]
        dp[price] = str(i)

    for i in range(n):
        if(dp[i]=="-1"):
            continue

        cur = dp[i]

        for j in range(n):
            price = prices[j]
            if (i+price <= m):
                new_number = ""
                idx = 0
                while idx <len(cur) and price<cur[idx]:
                    idx+=1
                new_number = cur[:idx]+str(j)+cur[idx:]

                if(len(new_number)>len(dp[i+price])):
                    dp[i+price] = new_number
                elif(len(new_number)==len(dp[i+price])):
                    idx == 0
                    while(idx < len(new_number)):
                        if(int(new_number[i])>int(dp[i+price][i])):
                            dp[i+price] = new_number
                            break
                        elif(int(new_number[i])<int(dp[i+price][i])):
                            break
                        else:
                            idx+=1
                 

    print(dp)
if __name__=="__main__":
    solve()