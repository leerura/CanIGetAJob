import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    grounds =[list(map(int,input().split())) for _ in range(n)]

    for ground in grounds:
        total = ground[0]
        dict = {}
        for i in range(1, len(ground)):
            soldier = ground[i]
            dict[soldier] = dict.get(soldier,0) +1

        
        
        war = True
        for s in dict.keys():
            if(dict[s] > total//2):
                print(s)
                war = False
                break
        if (war):
            print("SYJKGW")




if __name__ == "__main__":
    solve()