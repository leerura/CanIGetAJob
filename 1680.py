import sys

input = sys.stdin.readline

def solve():
    t = int(input().strip())

    for _ in range(t):
        w, n = map(int, input().split()) #w는 쓰레기 차 중량, n는 지점 개수
        trashes = [tuple(input().split()) for _ in range(n)]
        cur_weight = 0
        total_distance = 0
        cur_position = 0

        for trash in trashes:
            position, weight = map(int, trash)

            #일단 가
            total_distance += position-cur_position
            cur_position = position
            
            if(w > cur_weight + weight):
                cur_weight += weight
            elif(w==cur_weight + weight):
                total_distance += position
                cur_position = 0
                cur_weight=0
            elif(w < cur_weight + weight):
                #한 번 비워
                total_distance += position # 원점 가기
                total_distance += position # 다시 지점으로 오기
                cur_weight = weight

                if(w==cur_weight):
                    cur_weight = 0
                    total_distance += position
                    cur_position =0



        total_distance += cur_position
        print(total_distance)
if __name__ == "__main__":
    solve()