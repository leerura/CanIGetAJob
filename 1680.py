import sys

input = sys.stdin.readline

def solve():
    t_str = input().strip()
    if not t_str: return
    t = int(t_str)

    for _ in range(t):
        w, n = map(int, input().split())
        cur_weight = 0
        total_distance = 0
        cur_position = 0

        for _ in range(n):
            position, weight = map(int, input().split())

            # 1. 지점으로 이동
            total_distance += (position - cur_position)
            cur_position = position # 현재 위치 갱신
            
            if w > cur_weight + weight:
                cur_weight += weight
            
            elif w == cur_weight + weight:
                # [수정] 딱 맞으면 비우고 무게 초기화!
                total_distance += position
                cur_position = 0
                cur_weight = 0
            
            elif w < cur_weight + weight:
                # [수정] 비우러 갔다가(pos) 다시 옴(pos)
                total_distance += (position * 2)
                cur_weight = weight
                # 현재 위치(cur_position)는 여전히 position임 (돌아왔으니까)

                # [수정] 돌아와서 실었는데 하필 이게 딱 w라면?
                if w == cur_weight:
                    total_distance += position
                    cur_position = 0
                    cur_weight = 0

        # 마지막 복귀 (이미 0이면 0이 더해짐)
        total_distance += cur_position
        print(total_distance)

if __name__ == "__main__":
    solve()