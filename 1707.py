import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve():
    k = int(input().strip())

    for _ in range(k):

        v,e = map(int,input().split())

        adj = [[] for _ in range(v+1)]

        visited = [0]*(v+1)

        answer = True

        def dfs(start, color):
            # 1 or 2
            nonlocal visited
            visited[start] = color

            nonlocal adj
            nonlocal answer

            for neighbor in adj[start]:
                if not answer: return

                
                if(color == visited[neighbor]):
                    answer = False
                    return 
                
                
                if(visited[neighbor]==0):
                    new_color = 2 if color==1 else 1
                    dfs(neighbor, new_color)
    
        for i in range(e):
            a,b = map(int, input().split())

            adj[a].append(b)
            adj[b].append(a)
        for i in range(1, v + 1):
            if not answer: break # 이미 답 나왔으면 중단
            if visited[i] == 0:
                dfs(i, 1)

        print("YES" if answer else "NO")
        
if __name__=="__main__":
    solve()