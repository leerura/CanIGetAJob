import sys
from itertools import combinations

input = sys.stdin.readline

def solve():
    n = int(input())
    points =[tuple(map(int,input().split())) for _ in range(n)]

    max_area = 0

    for triangle in list(combinations(points,3)):
        area = get_triangle_area(triangle[0], triangle[1], triangle[2])
        max_area = max(max_area,area)
    
    print(max_area)
    return
    
def get_triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    area = abs((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)) / 2
    return area




if __name__=="__main__":
    solve()