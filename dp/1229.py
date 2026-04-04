import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    cur_idx = 1
    cur_value = 1
    h = []
    h.append(0)

    while(cur_value <=n ):
        h.append(h[cur_idx-1]+4*(cur_idx)-3)
        cur_idx += 1
        cur_value =h[cur_idx-1]+4*(cur_idx)-3


    visited = [0] * (n+1)

    q = deque()

    for hex_num in h:
        if(n==hex_num):
            print(1)
            return
        visited[hex_num] = 1
        if(hex_num==0):
            continue
        q.append((hex_num,1))

    

    while(q):
        cur_num, count = q.popleft()

        for hex_num in h:
            if(n==cur_num+hex_num):
                print(count+1)
                return
            if(cur_num+hex_num < n and not visited[cur_num+hex_num] != 0):
                visited[cur_num+hex_num] = count+1
                q.append((cur_num+hex_num,count+1))

        

    

    print(q)









    '''
    dp = [float('inf')] * (n+1)

    dp[0] = 0
    for i in range(1,n+1):

        for num in h:
            if(i-num<0): #정렬보장
                break
            if(dp[i-num]+1<dp[i]):
                dp[i] = dp[i-num]+1

            

    print(dp[n])
    '''


if __name__=="__main__":
    solve()