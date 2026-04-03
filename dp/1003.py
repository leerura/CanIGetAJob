import sys

input = sys.stdin.readline

def solve():
    t = int(input().strip())

    memo = [-1]*41
    memo[0] = (1,0)
    memo[1] = (0,1)

    for i in range(2,41):
        memo[i] = (memo[i-1][0] + memo[i-2][0],memo[i-1][1]+memo[i-2][1])
    

    for _ in range(t):
        zero = 0
        one = 0

        n = int(input().strip())
        
        print(*(memo[n]))

if __name__=="__main__":
    solve()