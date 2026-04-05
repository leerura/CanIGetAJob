import sys

input = sys.stdin.readline

def solve():
    n,s,m = map(int,input().split())

    volumes = list(map(int, input().split()))

    num_of_volumes = len(volumes)

    memo = dict()


    result = 0
    #max 인 경우만 따지면 됨
    def dfs(volume, idx):
        nonlocal result

        if(volume, idx) in memo:
            return memo[(volume,idx)]
        

        if idx== num_of_volumes:
            return volume
        
        res = -1
        
        if(m>=volume+volumes[idx]):
            res = max(res, dfs(volume+volumes[idx], idx+1))
        
        if(volume-volumes[idx] >= 0):
            res = max(res, dfs(volume-volumes[idx], idx+1))

        memo[(volume,idx)] = res
        return res
        
    dfs(s,0)

    print(memo[(s,0)])

    
    




if __name__=="__main__":
    solve()