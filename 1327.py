import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    start = list(map(int, input().split()))

    answer = [i for i in range(1,n+1)]

    def bfs(start):


        if start == answer:
            print(0)
            return True

        

        s = set() #방문 확인
        s.add(tuple(start))

        q = deque()
        q.append((start,0)) #배열, 변경횟수

        while(q):
            cur, count = q.popleft()

            for i in range(n-k+1):
                next_state = cur[:i] + cur[i:i+k][::-1] + cur[i+k:]
                if (not tuple(next_state) in s ):
                    s.add(tuple(next_state))
                    q.append((next_state,count+1))
                    if(next_state == answer):
                        print(count+1)
                        return True
        return False


    if(not bfs(start)):
        print(-1)

if __name__ == "__main__":
    solve()

