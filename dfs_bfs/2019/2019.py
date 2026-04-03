import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    adj = {}

    for _ in range(n):
        x1,y1,x2,y2 =map(int,input().split())
        adj.setdefault((x1,y1),[]).append((x2,y2))
        adj.setdefault((x2,y2),[]).append((x1,y1))


            

    visited = set()

    def bfs(start_x,start_y):
        num_of_points = 1

        visited.add((start_x,start_y))
        q = deque()
        q.append((start_x,start_y,None,None))

        while(q):
            cur_x,cur_y,parent_x,parent_y = q.popleft()
            if(len(adj.get((cur_x,cur_y),[])) != 2):
                return False

            for next_x,next_y in adj.get((cur_x,cur_y),[]):
                if(next_x == parent_x and next_y==parent_y):
                    continue


                if (not (next_x,next_y) in visited ):
                    visited.add((next_x,next_y))
                    q.append((next_x,next_y,cur_x,cur_y))
                    num_of_points+=1
                elif (next_x, next_y) in visited:
                    # [핵심] 부모가 아닌데 방문된 곳을 만났다? 
                    # BFS 경로가 어디서든 충돌했다는 뜻 = 사이클 존재 확정!
                    return True

        return False
            
        

    answer = 0

    for x,y in adj.keys():
        if(not (x,y) in visited ):
            if(bfs(x,y)):
                answer+=1

        
    print(answer)
    




if __name__=="__main__":
    solve()