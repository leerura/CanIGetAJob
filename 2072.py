import sys

input = sys.stdin.readline


def check_win(r,c, color,matrix):
    directions = [(0,1),(1,0),(1,1),(1,-1)]

    for dr, dc in directions:
        count = 1

        nr, nc = r+dr,c+dc

        while(0<=nr<19 and 0<=nc<19 and matrix[nr][nc]==color):
            count+=1
            nr += dr
            nc += dc

        nr, nc = r-dr,c-dc

        while(0<=nr<19 and 0<=nc<19 and matrix[nr][nc]==color):
            count+=1
            nr -= dr
            nc -= dc

        if(count == 5):
            return True
        
    return False

def solve():
    n = int(input().strip())

    matrix = [[0] * 19 for _ in range(19)] #0 두기 가능 ,1 black 2, white

    for i in range(n):
        row, col = map(int,input().split())
        row -= 1
        col -= 1
        
        color = 1 if i%2 == 0 else 2

        matrix[row][col] = color

        if(check_win(row,col,color, matrix)):
            print(i+1)
            return


    print(-1)

if __name__ =="__main__":
    solve()