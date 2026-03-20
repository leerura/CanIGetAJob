import sys
from collections import deque

input= sys.stdin.readline

def solve():
    n = int(input().strip())
    numbers = list(map(int,input().split()))
    k = int(input().strip())

    visited = set()

    def bfs(arr_numbers):
        
        q= deque()

        for number in arr_numbers:
            visited.add(number)
            q.append((number,1))


        while(q):
            cur_number, cur_count = q.popleft()
        

            for number in numbers:
                if(not cur_number+number in visited and cur_count+1 <= k):    
                    visited.add(cur_number+number)
                    q.append((cur_number+number,cur_count+1))

    bfs(numbers)

    target = 1
    while target in visited:
        target += 1

    if target % 2 != 0: # 홀수면 진학 승
        print(f"jjaksoon win at {target}")
    else: # 짝수면 상범 승
        print(f"holsoon win at {target}")

if __name__=="__main__":
    solve()