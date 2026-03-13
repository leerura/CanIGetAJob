import sys

inpput = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    maps = [list(input().strip()) for _ in range(n)]

    
    '''
        일단 모든 경우의 수를 다 따지자 n,m 모두 작아서 괜찮음
    '''
    max_size = 0
    for i in range(n):
        for j in range(m):
            size = 0
            for k in range(i,n):
                for l in range(j,m):
                    if((k-i)==(l-j) and maps[i][j] == maps[k][l] == maps[k][j] == maps[i][l]):
                        size = (k-i+1) * (k-i+1)
            max_size = max(max_size, size)


    print(max_size)

if __name__ == "__main__":
    solve()
