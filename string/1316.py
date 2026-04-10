import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    

    answer = 0

    for _ in range(n):
        word = input().strip()
        if(is_group(word)):
            answer +=1

    
    


    print(answer)

def is_group(w):
    s = set()
    

    s.add(w[0])

    length = len(w)

    
    for i in range(1,length):
        cur = w[i]
        prev = w[i-1]

        if (cur in s and cur!=prev):
            return False
        elif(cur not in s):
            s.add(cur)


    
    return True


    



if __name__=="__main__":
    solve()