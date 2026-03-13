import sys
from itertools import permutations

input  = sys.stdin.readline

def solve():
    n = int(input())
    how_many_on_the_left = list(map(int,input().split()))
    members = [i for i in range(1,n+1)]
    
    '''
    모든 경우의 수를 다 따질까?
    '''
    for available in list(permutations(members, n)):
        res = check(available, how_many_on_the_left)
        if(res):
            for i in range(len(res)):
                print(res[i], end=" ")

def check(member, how_many_on_the_left):
    n = len(member)

    for i in range(n):
        mem = member[i]
        left = how_many_on_the_left[mem-1]
        count = 0
        for j in range(0,i):
            if(member[j] > mem):
                count +=1
        if (count != left):
            return None
    return member
    
    

if __name__ == "__main__":
    solve()