import sys
from itertools import permutations

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    numbers = [i+1 for i in range(n)]
    data = list(map(int,input().split()))
    used_numbers = [False] *(n+1)

    def factorial(num):
        #향후 최적화 필요
        if(num==0 or num ==1):
            return 1
        
        return num*factorial(num-1)

    if(data[0]==1):
        k = data[1]

        
        answer = []
        count = 0 #k와 비교
        digits = 1
        while(True):
            if(len(answer)==n):
                break

            for i in range(1,n+1):
                if(not used_numbers[i]):
                    if(count+factorial(n-digits)>= k):
                        digits+=1
                        answer.append(i)
                        used_numbers[i] = True
                        break
                    else:
                        count += factorial(n-digits)
        print(*(answer))
    else:
        numbers = data[1:n+1]

        answer = 0

        for i in range(n):
            current_num = numbers[i]

            less_count = 0
            for j in range(1,current_num):
                if not used_numbers[j]:
                    less_count +=1

            answer += less_count * factorial(n-1-i)
            used_numbers[current_num] =True
            

        print(answer+1)



        





    """
    perm = list(permutations(numbers,n)) #이게 너무 많네... swap하는 알고리즘을 짜야할 것 같음
    perm.sort()
    
    if data[0] == 1:
        print(*(perm[data[1]-1]))
        return
    else:
        tu = tuple(data[1:n+1])
        for i in range(len(perm)):
            if(tu==perm[i]):
                print(i+1)
                return
    """

if __name__ == "__main__":
    solve()