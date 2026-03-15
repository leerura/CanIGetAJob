import sys
from itertools import combinations

input = sys.stdin.readline

def solve():
    n,s = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = 0
    for i in range(1,n+1):
        for com in list(combinations(numbers,i)):
            if(s==sum(com)):
                answer += 1
    print(answer)

    


if __name__=="__main__":
    solve()

