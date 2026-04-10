import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    words = []

    for _ in range(n):
        words.append(input().strip())

    words.sort()

    answer = 0
    

    for i in range(len(words)-1):
        cur_word = words[i]
        next_word = words[i+1]
        
        if not next_word.startswith(cur_word):
            answer += 1

    print(answer+1)

if __name__=="__main__":
    solve()