import sys

input = sys.stdin.readline

def solve():
    str = input().strip()
    dict = {}
    left = ""

    for s in str:
        dict[s] = dict.get(s,0) + 1

    number_of_odd = 0
    
    for key in dict.keys():
        if(dict[key] % 2 == 1):
            number_of_odd += 1
    
    
    if(number_of_odd >1):
        print("I'm Sorry Hansoo")
        return


    odd = ""
    for key in dict.keys():
        if(dict[key] % 2 == 1):
            odd = key



    for i in range(ord("A"), ord("Z")+1):
        char = chr(i)
        if char in dict.keys():
            left = left+char*(dict[char]//2)
            

    print(left+odd+left[::-1])

if __name__ == "__main__":
    solve()