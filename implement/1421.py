import sys

input = sys.stdin.readline

def solve():
    n, c, w = map(int, input().split()) #n: 나무의 개수, c: 나무 자를 때는 비용, w: 나무 한 단위의 가격


    woods = []
    
    max_wood = 0
    for _ in range(n):
        length = int(input().strip())
        woods.append(length)

        max_wood = max(length, max_wood)

    max_answer = 0

    for cut_length in range(1, max_wood+1):
        answer = 0
        for wood in woods:
            if(wood==cut_length):
                answer += wood*w
            elif(wood > cut_length):
                q = wood//cut_length
                if(wood%cut_length==0):
                    cuts = q-1
                else:
                    cuts = q
                if(q*cut_length*w-c*cuts>0):
                    answer += q*cut_length*w-c*cuts
               
        
        max_answer = max(answer, max_answer)
    print(max_answer)

if __name__ == "__main__":
    solve()