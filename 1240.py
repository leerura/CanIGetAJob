import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b,d = map(int,input().split())
        adj[a].append((b, d))
        adj[b].append((a, d))

    def dfs(start, end, d, visited):
        if start == end:
            return d
        
        visited[start] = True
        
        for neighbor, distance in adj[start]:
            if(not visited[neighbor]):
                visited[neighbor] = True
                
                result = dfs(neighbor,end,d+distance, visited)
                if result is not None:
                    return result

        return None
                
        
    for _ in range(m):
        start, end = map(int, input().split())
        visited = [False] * (n + 1)

        print(dfs(start, end, 0, visited))

if __name__ =="__main__":
    solve()
    
