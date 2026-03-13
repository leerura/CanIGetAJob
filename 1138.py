import sys
from itertools import permutations

input  = sys.stdin.readline

def solve():
    n = int(input())
    how_many_on_the_left = list(map(int,input().split()))
    answer = [0] * n
    for i in range(1, n+1):
        left = how_many_on_the_left[i-1]

        count = 0
        index = 0
        while(count < left or answer[index] != 0):
            if(answer[index]==0):
                count += 1
                index += 1
            else:
                index +=1
        answer[index] =i

    for a in answer:
        print(a, end=" ")
    
    

def solve_brute_force():
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