import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    def bfs(start,end):
        if start==end: 
            print(0)
            return
        

        visited = set()
        q = deque()

        q.append((start,0)) #위치, 횟수

        while(q):
            cur_position, cur_count = q.popleft()

            next_positions = [cur_position-1, cur_position+1, 2*cur_position]

            for next_position in next_positions:
                if(0<= next_position<=100000 and not next_position in visited):
                    if(next_position == end):
                        print(cur_count+1)
                        return
                    visited.add(next_position)
                    q.append((next_position, cur_count+1))

    bfs(n,k)



if __name__=="__main__":
    solve()