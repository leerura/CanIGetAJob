import sys

input = sys.stdin.readline

def solve():
    maps = [list(map(int, input().split())) for _ in range(5)]

    result_set = set()
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def dfs(start_row, start_col, number,count):
        if count==7:
            result_set.add(number)
            return
        
        for i in range(4):
            nr = start_row + dr[i]
            nc = start_col + dc[i]

            if(0<=nr<5 and 0<= nc<5 and number+str(maps[nr][nc]) not in result_set):
                dfs(nr,nc, number+str(maps[nr][nc]), count+1)
    
    for i in range(5):
        for j in range(5):
            dfs(i,j,"",1)

    print(len(result_set))

if __name__ == "__main__":
    solve()
    