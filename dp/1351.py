import sys

input = sys.stdin.readline

def solve():
    n,p,q = map(int, input().split())

    data = {}
    data[0] = 1

    #재귀 깊이가...
    def cal(num):
        nonlocal data
        if num in data:
            return data[num]
        
        
        first = num//p
        second = num//q
        data[num] = cal(first)+cal(second)
        
        
        return data[num]
    
    print(cal(n))

if __name__ == "__main__":
    solve()