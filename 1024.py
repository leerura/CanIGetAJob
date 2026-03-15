import sys

input = sys.stdin.readline

def solve():
    n, l = map(int,input().split())

    for i in range(l,101):
        numerator = n- i*(i-1)//2

        if(numerator < 0):
            break

        if numerator % i == 0: # x가 정수로 딱 떨어질 때
            x = numerator // i
            # 구한 수열 출력
            res = [x + j for j in range(i)]
            print(*(res))
            return
    print(-1)
    return


    for i in range(l,min(n,101)):
        q = n//i
        r = n%i
        if i%2==1 and r==0 and 0 <= q- (i-1)//2 and q+(i-1)//2 <= n :
            for i in range(q-(i-1)//2,q+(i-1)//2+1):
                print(i, end=" ")
            return
        if i%2==0 and r!=0 and 0 <= q- i//2+1 and  q+i//2 <= n:
            for i in range(q- i//2+1,q+i//2+1):
                print(i, end=" ")
            return

    print(-1)
    return
    



    
    numbers = [i for i in range(n//2)]

    
    answer = []
    min_length = float("inf")

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            res = sum(numbers[i:j+1])
            if(res == n and j+1-i >= l):
                length = j+1-i
                if(length < min_length):
                    answer = numbers[i:j+1]
    if(answer == []):
        print(-1)
        return
    for num in answer:
        print(num, end=" ")

    
if __name__ == "__main__":
    solve()