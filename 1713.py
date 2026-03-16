import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    m = int(input().strip())
    recommendations = list(map(int,input().split()))

    album = {}
    """
    album ={
        2 : {
            vote:
            time:
        }
    }
    
    """

    for i in range(len(recommendations)):
        
        """
        1. 이미 앨범에 있는가?
        있다면 그냥 up
        없다면

        2. 앨범에 없다면
        앨범이 현재 널널함 -> 추가
        앨범이 현재 꽉참 -> 삭제
        
        """
        recommendation = recommendations[i]

        if(recommendation in album.keys()):
            album[recommendation]["vote"] += 1
        else:
            if(len(album) < n):
                album[recommendation] = {}
                album[recommendation]["vote"] = 1
                album[recommendation]["time"] = i

            else:
                min_vote = float("inf")
                min_time = float("inf") #작을수록 오래됨
                del_key = ""
                for key in album.keys():
                    vote = album[key]["vote"]
                    if (min_vote > vote):
                        min_vote = vote
                        min_time = album[key]["time"]
                        del_key = key
                    elif min_vote == vote:
                        time = album[key]["time"]
                        if (time < min_time):
                            min_vote = vote
                            min_time = time
                            del_key = key
                del album[del_key]
                album[recommendation] = {}
                album[recommendation]["vote"] = 1
                album[recommendation]["time"] = i
    answer = sorted(list(album.keys()))
    print(*(answer))
                

    


if __name__ =="__main__":
    solve()