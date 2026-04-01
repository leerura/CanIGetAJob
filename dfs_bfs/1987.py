import sys

input = sys.stdin.readline

def solve():
    r,c = map(int, input().split())

    maps = []

    for _ in range(r):
        line = input().strip()
        maps.append(line)

    used_char = set() #set을 이렇게 관리해도 되나 싶긴하네
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    def dfs(row,col):
        res = 1
        used_char.add(maps[row][col])
        
        max_dist = 0
        for i in range(4):
            nr,nc = row+dr[i],col+dc[i]
            if(0<=nr<r and 0<=nc<c and not maps[nr][nc] in used_char):
                max_dist = max(max_dist, dfs(nr,nc))
        
        used_char.remove(maps[row][col])

        return res+max_dist
    
    print(dfs(0,0))



if __name__ =="__main__":
    solve()