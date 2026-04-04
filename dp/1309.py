import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    dp = [[0] * 3 for _ in range(n)] #10만 행 생성...

    prev0 = 1
    prev1 = 1
    prev2 = 1

    cur0 = 1
    cur1 = 1
    cur2 = 1



    for _ in range(1,n):
        cur0 = (prev0+prev1+prev2)%9901
        cur1 = (prev0+prev2)%9901
        cur2 = (prev0+prev1)%9901

        prev0 = cur0
        prev1 = cur1
        prev2 = cur2




    print((cur0+cur1+cur2)%9901)

    

if __name__=="__main__":
    solve()