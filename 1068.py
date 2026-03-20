import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    children = [[] for _ in range(n)] #i번째의 자식들
    visited = [False] * n

    parents = list(map(int, input().split()))

    root = 0

    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    


    remove = int(input().strip())
    if(remove == root):
        print(0)
        return

    for i in range(n):
        if(parents[i] == -1): continue
        if i == remove: continue

        children[parents[i]].append(i)

    

    leaf_count = 0
    def dfs(start):
        nonlocal leaf_count
        visited[start]=True

        if children[start]==[]:
            leaf_count += 1

        for child in children[start]:
            if(not visited[child]):
                visited[child]
                dfs(child)

    dfs(root)
    print(leaf_count)





if __name__ == "__main__":
    solve()