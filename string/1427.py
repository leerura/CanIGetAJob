import sys

input = sys.stdin.readline

def solve():
    n = input().strip()

    num_list = list(map(int, list(n)))

    num_list.sort(reverse=True)

    for digit in num_list:
        print(digit, end="")
    


if __name__=="__main__":
    solve()