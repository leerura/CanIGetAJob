import sys

input = sys.stdin.readline

def solve():
    xs, ys = map(int, input().split())
    xe, ye, dx, dy = map(int, input().split())


    t = (xe*dx + ye*dy)/(dx**2+dy**2)
    print(t)
    

if __name__=="__main__":
    solve()