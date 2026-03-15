import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    moves = list(input())


    positions = [(0,0)]
    
    
    cur_r = 0
    cur_c = 0
    cur_direction = 0 #0 남 1 서 2 북 3동

    for move in moves:
        if(move == "F"):
            if(cur_direction == 0):
                cur_r += 1
            elif(cur_direction == 1):
                cur_c -= 1
            elif(cur_direction == 2):
                cur_r -= 1
            elif(cur_direction == 3):
                cur_c +=1
            positions.append((cur_r, cur_c))
        elif(move == "R"):
            cur_direction = (cur_direction+1)%4
        elif(move == "L"):
            cur_direction = (cur_direction-1)%4
        
    min_r = float("inf")
    max_r = float("-inf")
    min_c = float("inf")
    max_c = float("-inf")
    for position in positions:
        r, c = position
        min_r = min(r, min_r)
        max_r = max(r, max_r)
        min_c = min(c, min_c)
        max_c = max(c, max_c)

    len_row = max_r-min_r+1
    len_col = max_c-min_c+1

    answer = [["#"] * len_col for _ in range(len_row)]

    

    for i in range(len(positions)):
        r, c = positions[i]
        positions[i] = r - min_r , c-min_c
        
    for position in positions:
        r,c = position
        answer[r][c] = "."
    


    for row in answer:
        print("".join(row))
        
if __name__ == "__main__":
    solve()
    