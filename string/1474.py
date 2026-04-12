import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    words =[]

    length = 0

    

    for _ in range(n):
        word = input().strip()
        length += len(word)
        words.append(word)
        
        

    if n == 1: # 단어가 하나일 땐 그냥 출력
        print(words[0])
        return
    

    base_count = (m-length)//(n-1)
    extra_count = (m-length)%(n-1)

    gap = ["_"*base_count] * (n-1) #gap[i] => words[i] 뒤에 오는 인덱스 개수

    add_time=0
    already = [False] * (n-1)

    for i in range(n-1):
        
        if(words[i+1][0]>"_" and add_time<extra_count):
            
            gap[i] = gap[i]+"_"
            add_time += 1
            already[i] = True



    #얘가 쫌 그러네
    cur = n-2
    while(add_time <extra_count and cur>=0):
        if(not already[cur]):
            already[cur] = True
            words[cur] = words[cur]+"_"
            add_time +=1
            cur -= 1
        else:
            cur-=1
    


    for i in range(n):
        if(i!=(n-1)):
            print(words[i]+gap[i], end="")
        else:
            print(words[i])
    


    '''
    add_time=0
    for i in range(len(words)):
        cur = words[i]

        if(i==len(words)-1):
            print(cur)
            continue

        if(words[i+1][0]>"_" and add_time<(m-length)%(n-1)):#소문자라면
            print(cur+"_"*((m-length)//(n-1)+1), end="")
            add_time+=1
            continue



        print(cur+"_"*((m-length)//(n-1)), end="")

    '''

    #print("몇 번 넣을까?", n-1)
    #print("몇 개씩 넣어?", (m-length)//(n-1))
    #print("몇 군데 추가로 넣을까?", (m-length)%(n-1))


    


if __name__=="__main__":
    solve()