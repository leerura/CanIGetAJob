import sys

input = sys.stdin.readline

def solve():
    board = input().strip()

    length = len(board)
    cur = 0

    answer =""

    while(cur<length):
        #지금 칸을 덥어야하나?
        if(board[cur]=="."):
            cur +=1
            answer += "."
            continue
        else:
            #현재부터 해서 A로 덥을 수 있는가?
            if(cur+3 < length and board[cur:cur+4]=="XXXX"):
                answer += "AAAA"
                cur += 4
            elif(cur+1 < length and board[cur:cur+2]=="XX"):
                answer += "BB"
                cur += 2
            else:
                print(-1)
                return
    print(answer)

    
if __name__=="__main__":
    solve()