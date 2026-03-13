import sys

input = sys.stdin.readline

def solve():
    king, stone, n = input().split()
    n = int(n)
    moves = [input().strip() for _ in range(n)]

    dict ={
        "R" : (1,0),
        "L" : (-1,0),
        "B":  (0,-1),
        "T": (0,1),
        "RT":(1,1),
        "LT":(-1,1),
        "RB":(1,-1),
        "LB":(-1,-1)
    }

    x_of_king = ord(king[0])
    y_of_king = int(king[1])

    x_of_stone = ord(stone[0])
    y_of_stone = int(stone[1])
    
    for move in moves:
        dx,dy = dict[move]
        nxk, nyk = x_of_king+dx, y_of_king + dy

        if(nxk == x_of_stone and nyk==y_of_stone):
            nxs ,nys = x_of_stone+dx, y_of_stone+dy
        else:
            nxs ,nys = x_of_stone, y_of_stone

        if(ord("A")<=nxk <= ord("H") and 1<=nyk <= 8 and ord("A")<=nxs <= ord("H") and 1<=nys <= 8):
            x_of_king = nxk
            y_of_king = nyk
            x_of_stone = nxs
            y_of_stone = nys
    
    print(chr(x_of_king)+str(y_of_king))
    print(chr(x_of_stone)+str(y_of_stone))
        

    


if __name__ =="__main__":
    solve()


