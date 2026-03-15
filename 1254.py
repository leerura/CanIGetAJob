import sys

input = sys.stdin.readline

def solve():
    s = input().strip()
    if(is_pelindrome(s)):
        print(len(s))
        return
    for i in range(len(s)):
        new_str = s+ s[i::-1]
        if(is_pelindrome(new_str)):
            print(len(new_str))
            return

    

def is_pelindrome(str):
    left = 0
    right = len(str)-1
    while(left<=right):
        if(str[left]!=str[right]):
            return False
        left += 1
        right -= 1
    return True

if __name__=="__main__":
    solve()
