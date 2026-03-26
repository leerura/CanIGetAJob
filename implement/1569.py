import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    start_x, start_y = map(int, input().split())

    left = start_x
    right = start_x
    top = start_y
    bottom = start_y

    points = []
    points.append((start_x,start_y))

    for _ in range(n-1):
        x,y = map(int,input().split())
        
        left = min(left,x)
        right = max(right,x)

        top = max(top,y)
        bottom = min(bottom,y)

        points.append((x,y))

    l = max(right-left, top-bottom)
    if (l==0):
        print(-1)
        return
    
    candidates = [
        (left,bottom),
        (right-l,bottom),
        (left,top-l),
        (right-l, top-l)
    ]

    for X,Y in candidates:
        is_ok = True
        for px, py in points:

            on_boundary = (
                ((px == X or px == X + l) and Y <= py <= Y + l) or
                ((py == Y or py == Y + l) and X <= px <= X + l)
            )
            if not on_boundary:
                is_ok = False
                break
        if is_ok:
            print(l)
            return
    print(-1)
    return

    if(left==right and top==bottom):
        print(-1)
        return
    
    if(left==right or top==bottom):
        print(max(right-left, top-bottom))
        return
    
    def available(left,right,top, bottom):
        avail = True
        for x,y in points:
            if(not (x==left or x == right or y==top or y==bottom)):
                return False
        return avail
    
    width = right-left
    height = top-bottom
    if(width > height):
        if(available(left, right, top+width-height, bottom) or available(left,right, top, bottom-width-height) ):
            print(width)
            return
        
    elif(width < height):
        if(available(left-height-width, right, top, bottom) or available(left,right+height-width, top, bottom)):
            print(height)
            return
    else:
        if(available(left,right,top,bottom)):
            print(width)
            return
    print(-1)
    
if __name__=="__main__":
    solve()