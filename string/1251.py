import sys
from itertools import combinations

input = sys.stdin.readline

def solve():
    word = input().strip()

    indices = [i for i in range(len(word)-1)]

    comb = combinations(indices,2)

    min_res = None

    for idx1, idx2 in list(comb):

        res = word[:idx1+1][::-1] + word[idx1+1:idx2+1][::-1]+word[idx2+1:][::-1]
        if min_res is None or res<min_res:
            min_res = res



    print(min_res)

    """
    아래 방법은 정답을 보장할 수 가 없음... bruteforce로 갑니다.
    first = ord('z')
    first_idx = 0

    for i in range(len(word)):
        chr = word[i]
        if(first>= ord(chr)): #같을 때도 고려해야겠다 => 
            first_idx = i
            first = ord(chr)
  

    second = ord('z')
    second_idx = first_idx

    for i in range(first_idx,len(word)):
        chr = word[i]
        if(second>= ord(chr) and first<ord(chr)): #같을 때도 고려해야겠다
            second_idx = i
            second = ord(chr)


    one = word[first_idx::-1]
    
    two=word[second_idx:first_idx:-1]
    three = word[:second_idx:-1]

    print(one+two+three)
    """

   





if __name__=="__main__":
    solve()