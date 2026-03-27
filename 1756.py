import sys

input = sys.stdin.readline

def solve():
    d,n = map(int, input().split()) #최대 30만, 

    diameters = list(map(int,input().split()))
    diameters.append(0)

    pizzas = list(map(int,input().split()))

    used = [False] * (d+1)
    
    used[d]= True

    pointer = d

    #이 중 for문은 쫌.... 30만 제곱은 900억...
    for i in range(n):

        if(used[0]):
            print(0)
            return
        
        pizza = pizzas[i]
        
        #직접 넣어봅시다.

        is_available = False

        for j in range(pointer): #이런식으로 해도 되나?
            cur_diameter = diameters[j]
            if(cur_diameter>= pizza and (diameters[j+1]<pizza or used[j+1])):#인덱스 out of range 고려
                used[j] = True
                pointer = j
                is_available = True
                break
        if(not is_available):
            print(0)
            return

    
    for i in range(n):
        if(used[i]):
            print(i+1)
            return



if __name__ == "__main__":
    solve()

