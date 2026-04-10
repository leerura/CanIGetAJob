import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    data = {}

    for _ in range(n):
        book = input().strip()

        data[book] = data.get(book,0)+1



    max_value = 0
    best = ""
    for key in data.keys():
        if(max_value < data[key]):
            max_value = data[key]
            best = key
        elif max_value == data[key] and key<best :
            best = key

    print(best)




if __name__=="__main__":
    solve()