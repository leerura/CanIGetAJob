import sys
from collections import deque

input = sys.stdin.readline

def solve():
    d, start_word = input().split()
    d = int(d)

    data = {
    }

    for _ in range(d):
        word = input().strip()
        length = len(word)

        data.setdefault(length, []).append(word)

    visited = set()
    def bfs(start):
        nonlocal visited
        q = deque()
        
        visited.add(start)
        q.append(start)

        while(q):
            cur_word = q.popleft()
            cur_length = len(cur_word)

            words = data.get(cur_length+1, [])

            for word in words:
                if(changable(cur_word, word) and not word in visited):
                    visited.add(word)
                    q.append(word)
               
    def changable(str1, str2):
        n = len(str2)

        for i in range(n):
            str2_without_i = str2[:i]+str2[i+1:]
            if(str1 == str2_without_i):
                return True
        return False
    
    bfs(start_word)
    max_length = 0
    answer = ""

    for element in visited:
        length = len(element)
        if(length > max_length):
            max_length = length
            answer = element
    print(answer)
        



        


if __name__=="__main__":
    solve()