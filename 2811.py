import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    days = list(map(int, input().split()))
    """
    가장 쉬운순서부터 해보자
    1. 최장 우울 기간 1개, 겹치는 거 없음
    2. 겹치거나 앞에 삐져나가는 게 있음 but 최장 우울 기간은 1개
    3. 겹치거나 앞에 삐져나가는 것도 있고 최장 우울 기간도 2개 이상
    """

    flowers = [False] * n
    depressed = []
    
    max_t = 0
    i = 0
    while (i < n):
        if(days[i] < 0):
            start = i
            while i<n and days[i]<0:
                i+=1
            length = i-start
            depressed.append((start,length))
            max_t = max(max_t, length)
        else:
            i += 1

    for start, length in depressed:
        #만약 첫날부터 우울하면 어떡하지
        flower_start = max(0, start - 2 * length)
        

        for i in range(flower_start, start):
            flowers[i] = True

    base_flower_count = sum(flowers)

    max_extra = 0

    for start, length in depressed:
        if(length==max_t):
            current_extra = 0

            check_start = max(0, start - 3 * length)
            check_end = max(0, start - 2 * length)
            

            for j in range(check_start, check_end):
                if not flowers[j]: # 원본에서 False였던 곳만 카운트
                    current_extra += 1
            
            max_extra = max(max_extra, current_extra)
       
    print(base_flower_count + max_extra)
    

if __name__ == "__main__":
    solve()