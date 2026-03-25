import sys

input = sys.stdin.readline

def solve():
    a,b = map(int, input().split())

    n = int(input().strip())

    moves = input().strip()

    data = {
        "R" : (1,0),
        "L" : (-1,0),
        "U" : (0,1),
        "D" : (0, -1)
    }

    cur_x = 0
    cur_y = 0
    

    start = -1
    end = -1
    is_out = False
    for i in range(len(moves)):
        dx,dy = data[moves[i]]

        cur_x += dx
        cur_y += dy

        currently_outside = (cur_x < 0 or cur_x > a or cur_y < 0 or cur_y > b)

        

        if currently_outside and not is_out:
            start = i
            is_out = True
        elif not currently_outside and is_out:
            end = i-1
            is_out = False

        
    if is_out:
        end = len(moves) - 1
           
    if start != -1:
        print(start+1, end+1)
    else:
        print(0,0)
        

        


if __name__ =="__main__":
    solve()