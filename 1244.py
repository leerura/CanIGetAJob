import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    switches = list(map(int, input().split()))
    switches = [0] + switches
  

    students = int(input().strip())

    for _ in range(students):
        gender, number = map(int, input().split())

        if gender == 1:
            cur = number
            while (cur<= n):
                switches[cur] = 0 if switches[cur]==1 else 1
                cur = cur + number
        else:
            switches[number] = 0 if switches[number]==1 else 1
            left = number-1
            right = number+1
            while(left >= 1 and right <=n):
                if(switches[left] != switches[right]):
                    break
                else:
                    switches[left] = 0 if switches[left]==1 else 1
                    switches[right] = 0 if switches[right]==1 else 1
                    left -=1
                    right +=1
    for i in range(1,n+1,20):
        print(*(switches[i : i + 20]))
        
if __name__=="__main__":
    solve()