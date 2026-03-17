import sys
from collections import deque

input = sys.stdin.readline

def solve():
    '''
    동일한 우선 순위가 없을 때는 그냥 우선순위 큐만 쓰면 됨.
    근데 동일한 우선순위가 있다면 큐 맨뒤로 보내는 것을 구현해야함. => 우선순위큐를 사용하지 않겠음
    '''
    t = int(input().strip())
    for i in range(t):

        n, document = map(int, input().split())
        priorities = list(map(int, input().split()))

        queue = deque()

        for i in range(len(priorities)):
            #(번호, 우선순위)
            queue.append((i,priorities[i]))

        count = 0
        while(queue):
            cur_number, cur_priority = queue.popleft()
            
            go_back = False
            for num, priority in list(queue):
                if(priority > cur_priority):
                    queue.append((cur_number, cur_priority))
                    go_back = True
                    break

            if not go_back:
                count += 1
                if (cur_number == document):
                    print(count)

if __name__ =="__main__":
    solve()