import sys

input = sys.stdin.readline

def solve():
    n,p,q,x,y = map(int, input().split())

    memo = {}
    memo[0] = 1

    def cal(num):
        if num in memo:
            return memo[num]
        if num<=0:
            return 1
        
        memo[num] = cal(num//p-x)+cal(num//q-y)
        
        return memo[num]
    
    print(cal(n))

if __name__=="__main__":
    solve()