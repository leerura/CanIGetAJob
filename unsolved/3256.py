import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    distance = [0] * n
    end_time = [0] * n

    first = int(input().strip())
    distance[0] = first
    end_time[0] = first +4

    for i in range(1, n):
        cur = int(input().strip())
        before = distance[i-1]

        arrival = cur + i

        for j in range(i): # 내 앞의 모든 승객 j에 대하여
            prev_R = distance[j]
            prev_end = end_time[j]
    
            if prev_R < cur:
                # 내 앞사람이 내 길목(prev_R)에서 짐을 넣는 경우
                # 내가 그 칸(prev_R)을 통과할 수 있는 시간은 (prev_end + 1)
                # 거기서 내 자리(cur)까지 남은 거리만큼 더 가야 함
                arrival = max(arrival, prev_end + 1 + (cur - prev_R))
            else:
                # 내 앞사람이 나보다 더 멀리(prev_R) 가서 짐을 넣는 경우
                # 나는 앞사람보다 최소 (i-j)초는 늦게 도착함 (줄 서서 가니까)
                # 앞사람이 내 자리(cur)를 통과한 시간 + (i-j)
                prev_arrival = prev_end - 4
                prev_pass_my_seat = prev_arrival - prev_R + cur
                arrival = max(arrival, prev_pass_my_seat + (i - j))

        distance[i] = cur
        end_time[i] = arrival + 4

    answer = 0
    for i in range(n):
        answer = max(answer, end_time[i])
    print(answer)




if __name__=="__main__":
    solve()