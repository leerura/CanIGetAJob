import sys

input = sys.stdin.readline

def solve():
    s = input().strip()


    length = len(s)

    #0->1
    zero_to_one = 0
    for i in range(length):
        cur = s[i]
        prev = s[i-1] if i!=0 else None
        if(cur=="0" and (not prev=="0" or None)):
            zero_to_one+=1

    one_to_zero=0
    for i in range(length):
        cur = s[i]
        prev = s[i-1] if i!=0 else None
        if(cur=="1" and (not prev=="1" or None)):
            one_to_zero +=1

    print(min(zero_to_one,one_to_zero))

if __name__=="__main__":
    solve()

        