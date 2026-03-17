import sys
import math

input = sys.stdin.readline



def solve():
    t, x, m = map(int, input().split()) # t 시간, x개의를 담을 수 있음, m개의 몬스터가 잇음
    monsters = [tuple(map(int,input().split())) for _ in range(m)] #(d,s) = (최대 거리, 속도)
    cur_distances = [monsters[_][0] for _ in range(m)]

    """
    최대를 어떻게 구할까 최대.... 그리디 아닌가? 지금 먹었을 때 ㄱㅊ은지 보고 아니면 먹지말고 하면 되지 않나? 먹을 수 있을 때 먹자
    시간 초과 현재 billions여서 부담스럽긴함.... 어떻게 최적화를 하지?
    어디가 비효율적일까?
    모든 몬스터를 저렇게 신경써야할까? 가장 위협이 되는 친구만 신경쓰면 안되나? 
    나에게 가장 빨리 다가올 수 있는 몬스터가 누구일까?
    근데 얼마나 멀리까지 갈 수 있는지도 알아야해서...
    그래도 일단 나한테 가장 빨리 다가올 수 있는 몬스터만 고려해보겠음
    그냥 처음에만 가장 위험한 친구를 고려하고
    그뒤로는 1초 쉬고 먹고 쉬고 먹고 하면 될 거 같음
    """
    if(m==0):
        print(t*x)
        return
    min_time = float("inf")
    fastest_monster = 0
    for i in range(m):
        
        distance, velocity = monsters[i]
        time = (distance-1)//2
        if time < min_time:
            fastest_monster = i
            min_time = time
    
    remain = (t-min_time)//2
    print((min_time+remain)*x)
    return


    count = 0
    for i in range(t):
        available = True
        
        after_distance = cur_distances[fastest_monster] - monsters[fastest_monster][1]
        if(after_distance <=0):
            available = False
            break

        if(available):
            count += 1
            
            cur_distances[fastest_monster] = cur_distances[fastest_monster] - monsters[fastest_monster][1]
        else:
            
            cur_distances[fastest_monster] = cur_distances[fastest_monster] + monsters[fastest_monster][1]
            if (cur_distances[fastest_monster] > monsters[fastest_monster][0]):
                cur_distances[fastest_monster] =monsters[fastest_monster][0]

    print(x*count)
    return


    count = 0
    for i in range(t):
        available = True
        for i in range(m):
            after_distance = cur_distances[i] - monsters[i][1]
            if(after_distance <=0):
                available = False
                break
        if(available):
            count += 1
            for i in range(m):
                cur_distances[i] = cur_distances[i] - monsters[i][1]
        else:
            for i in range(m):
                cur_distances[i] = cur_distances[i] + monsters[i][1]
                if (cur_distances[i] > monsters[i][0]):
                    cur_distances[i] =monsters[i][0]

    print(x*count)


if __name__ == "__main__":
    solve()