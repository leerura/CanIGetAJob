import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    

    s = set()

    for _ in range(n):
        option = input().strip()
        words = option.split()
        found = False
        

        for i in range(len(words)):
            key = words[i][0].upper()
            if key not in s:
                s.add(key)
                words[i] = "[" + words[i][0] + "]" + words[i][1:]
                found = True
                break
        if not found:
            for i in range(len(words)):
                for j in range(len(words[i])):
                    key = words[i][j].upper()
                    if key not in s:
                        s.add(key)
                        words[i] = words[i][:j] + "[" + words[i][j] + "]" + words[i][j+1:]
                        found = True
                        break
                if found: break
        
        print(" ".join(words))


if __name__ =="__main__":
    solve()