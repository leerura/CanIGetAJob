import sys

input = sys.stdin.readline

def solve():
    numbers = input().strip()
    n =1
    idx =0

    while(idx<len(numbers)):
        
        str_n = str(n) 
        
        for char in str_n:
            if(idx<len(numbers) and char == numbers[idx]):
                idx +=1
        n+=1
    print(n-1)


        
    

if __name__=="__main__":
    solve()