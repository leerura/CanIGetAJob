import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    names = []

    s = set()
    for i in range(n):
        name = input().strip()
        names.append(name)

        s.add(str(i+1)+" A")
        s.add(str(i+1)+" B")

    for _ in range(2*n-1):
        number_chr = input().strip()
        s.remove(number_chr)

    for loser_chr in s:
        loser, chr = loser_chr.split()
        print(loser+ " " + names[int(loser)-1])

if __name__=="__main__":
    solve()

    