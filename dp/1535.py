import sys

input = sys.stdin.readline
#경우의 수가 2^20이여서 굳이 메모를 안해도 되긴함.

def solve():
    n = int(input().strip())
    loose = list(map(int, input().split()))
    get = list(map(int, input().split()))

    memo = {}

    def dfs(hp, happy, idx):
        if (hp,happy,idx) in memo.keys():
            return memo[(hp,happy,idx)]
    
        if(hp<=0):
            return 0
        
        if(idx==n):
            return happy
        
        res = 0
        
        #인사함
        res = max(res,dfs(hp-loose[idx], happy+get[idx], idx+1))

        #pass 함
        res = max(res,dfs(hp, happy, idx+1))

        memo[(hp,happy,idx)]=res


        return res
    
    print(dfs(100,0,0))

if __name__=="__main__":
    solve()