import sys

input = sys.stdin.readline

def solve():
    document = input().strip()
    query = input().strip()

    if(len(query)>len(document)):
        print(0)
        return



    answer = 0


    idx = 0
    while(idx <=len(document)-len(query)+1):
        if(document[idx:idx+len(query)]==query):
            answer+=1
            idx+=len(query)
        else:
            idx+=1
    


    print(answer)


if __name__=="__main__":
    solve()