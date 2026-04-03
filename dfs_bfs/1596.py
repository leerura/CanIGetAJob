import sys

input = sys.stdin.readline


def sik(number):
    str_num = str(number)
    answer = ""
    for i in range(len(str_num)-1):
        diff = str(abs(int(str_num[i])-int(str_num[i+1])))
        answer = answer + diff
    #00은 okay인데 만약 01이면? 걍 다 쳐내고 빈 배열이면 0으로 나타내는 걸로하자

    p = 0
    if(answer[0] == "0"):
        while p<len(answer)and answer[p] == "0":
            p+=1

    

    answer = answer[p:]
    if(answer ==""):
        answer = "0"

    return int(answer)

    
"""
일단 모든 경우를 다 확인하면 최소 10억임... 즉 10초 ㅋㅋ
1. 메모를 해야할까? 그렇다고 효율적이어질까? 일단 해보자. 근데 메모를 해도 전체를 도는 건데 그럼... 흠
2. 모든 경우의 수를 따지니 매우 비효율적으로 생각됨 오히려 7에서 거꾸로 올라갈수는 없을까? 
"""
memo = {}

def solve():
    a,b = map(int, input().split())
    answer = 0

    

    for num in range(a,b+1):
        cur = num
        while(len(str(cur)) > 1):
            cur = sik(cur)

        if(cur==7):
            answer+=1

    print(answer)


if __name__ =="__main__":
    solve()
    
    
    