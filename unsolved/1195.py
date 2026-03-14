import sys

input = sys.stdin.readline

def solve():
    '''
    1. 내부에서 맞물릴 경우
    2. 내부에서 해결이 안되어 튀어 나갈 경우...
    => 일단 1번 만이라도 해보자. 즉 내부로 해결할 수 있는지 판단
    '''
    a = input().strip()
    b = input().strip()
    len_a = len(a)
    len_b = len(b)

    min_len = len_a + len_b
    


if __name__ == "__main__":
    solve()