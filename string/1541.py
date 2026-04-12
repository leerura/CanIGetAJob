import sys

input = sys.stdin.readline

def solve():
    equation = list(input().split("-"))


    answer = sum(map(int,equation[0].split("+")))
    
    for i in range(1, len(equation)):
        answer -= sum(map(int,equation[i].split("+")))

    print(answer)

if __name__=="__main__":
    solve()
