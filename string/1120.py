import sys


input = sys.stdin.readline

def solve():
    a, b = input().split()    
    
    diff = len(b)-len(a)

    min_value = 51
    for i in range(diff+1):
        comp = b[i:i+len(a)]


        value = 0
        
        for j in range(len(a)):
            if(a[j]!=comp[j]):
                value += 1
     
    
        min_value = min(min_value,value)
        

    print(min_value)

if __name__=="__main__":
    solve()