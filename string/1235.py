import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    numbers = []

    for _ in range(n):
        number = input().strip()
        numbers.append(number)

    
    k = 1
    

    
    while k<=len(numbers[0]):
        s = set()
        available  = True
        for number in numbers:
            cut = number[-k:]
            if cut in s:
                 available = False
                 break
            else:
                 s.add(cut)
        
        if(available):
             print(k)
             break
             
        else:
             k += 1
            
    

if __name__=="__main__":
    solve()