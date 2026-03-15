import sys
from itertools import permutations
from collections import Counter

input = sys.stdin.readline


def solve():
    str = input().strip()
    counter = Counter(str)
    
    answer = 0

    
    for s in list(permutations(str,len(str))):
        if(is_lucky(s)):
            answer+=1

    for key in counter.keys():
        answer = answer//factorial(counter[key])

    

    print(answer)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)




def is_lucky(s):
    for i in range(1,len(s)):
        if(s[i-1]==s[i]):
            return False
    return True

if __name__=="__main__":
    solve()