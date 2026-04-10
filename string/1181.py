import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    data = {}

    min_length = 50
    max_length = 0

    for _ in range(n):
        word = input().strip()

        len(word)
        min_length = min(min_length,len(word))
        max_length = max(max_length,len(word))

        if(word not in data.setdefault(len(word),[])):
            data.setdefault(len(word),[]).append(word)


    for i in range(min_length,max_length+1):
        words = data.get(i,[])

        words.sort()

        for word in words:
            print(word)



if __name__=="__main__":
    solve()