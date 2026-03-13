import sys

input = sys.stdin.readline

def solve():
    
    
    line = input().split()
    
        
    a = int(line[0])
    b = int(line[1])
        
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")
    

if __name__ == "__main__":
    solve()