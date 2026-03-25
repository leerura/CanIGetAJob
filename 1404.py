import sys

input = sys.stdin.readline

def solve():
    data = list(map(int, input().split()))
    probs = [x/100 for x in data]

    matrix = [[0.0] * 8 for _ in range(8)]

    dp = [[0.0]* 8 for _ in range(4)] #dp[round][number] 특정라운드에서 number가 이길 확률
    for i in range(8):
        dp[0][i] = 1

    idx =0
    for i in range(8):
        for j in range(i+1,8):
            matrix[i][j] = probs[idx]
            matrix[j][i] = 1-probs[idx]
            idx += 1

    


    for i in range(4):
        left = 2*i
        right = 2*i+1

        dp[1][left] = matrix[left][right]
        dp[1][right] = matrix[right][left]

        round = 1
        size = 2**round
        half = size//2

        dp[1][left] = matrix[left][right]
        dp[1][right] = matrix[right][left]

        


    for i in range(4):
        left = 2*i
        right = 2*i+1

        round=2
        size = 2**round#4명
        half = size//2#2명의 결과

        if(i==0):
            k =1
        elif(i==1):
            k=0
        elif(i==2):
            k=3
        elif(i==3):
            k=2

        opp_start = k*2
        opp_end = opp_start+half

        win_sum_left = 0
        win_sum_right = 0

        for j in range(opp_start, opp_end):
            # 상대 j가 올라올 확률 * 내가 j를 이길 확률을 누적
            win_sum_left += dp[1][j] * matrix[left][j]
            win_sum_right += dp[1][j] * matrix[right][j]
        
        dp[2][left] = dp[1][left] * win_sum_left
        dp[2][right] = dp[1][right] * win_sum_right

    for i in range(4):
        left = 2*i
        right = 2*i+1

        if(i==0 or i==1):
            k = 2
            
        else:
            k = 0
        
        round = 3
        size = 2**round
        half = size//2

        opp_start = 2*k
        opp_end = opp_start+half

        win_sum_left = 0
        win_sum_right = 0

        for j in range(opp_start,opp_end):
            win_sum_left += dp[2][j]*matrix[left][j]
            win_sum_right += dp[2][j]*matrix[right][j]

        dp[3][left] = dp[2][left]*win_sum_left
        dp[3][right] = dp[2][right]*win_sum_right



    print(*(dp[3]))

if __name__=="__main__":
    solve()