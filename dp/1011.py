import sys
import math

input = sys.stdin.readline

def is_perfect_square(n):
    if n<0: return False
    root = math.isqrt(n)
    return root*root == n

def solve():
    t = int(input().strip())

    for _ in range(t):
        x,y = map(int,input().split())

        l = y-x
        answer = 0
        if (is_perfect_square(l)):
            answer =math.isqrt(l)*2-1
        else:
            k = math.isqrt(l)
            if(k**2<l<=k**2+k):
                answer = 2*k
                
            else:
                answer = 2*k+1

        print(answer)
        

        

if __name__=="__main__":
    solve()