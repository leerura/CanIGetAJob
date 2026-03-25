import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, r1, c1, r2, c2 = map(int, input().split())

   
    for row in range(r1,r2+1):
        for col in range(c1, c2+1):
            nr = row
            nc = col
            if(row>2*n-2):
                nr = row % (2*n-1)
            if(col>2*n-2):
                nc = col % (2*n-1)

            dr = abs(nr -(n-1))
            dc = abs(nc-(n-1))

            if(dr+dc>=n):
                print(".", end="")
            else:
               
                print(chr(ord("a")+(dr+dc)%26), end="")

        
        print()



if __name__ =="__main__":
    solve()