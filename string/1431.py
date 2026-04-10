import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    serials = []

    for _ in range(n):
        serials.append(input().strip())

    serials.sort(key = lambda x : (len(x),number_of(x),x))



    for serial in serials:
        print(serial)

def number_of(s):
    answer = 0
    for i in range(len(s)):
        if s[i].isdigit():
            answer += int(s[i])

    return answer

        


if __name__=="__main__":
    solve()