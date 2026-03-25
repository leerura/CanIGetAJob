import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    words = []

    for _ in range(n):
        words.append(input().strip())

    answer = 0

    for i in range(n):
        for j in range(i+1,n):
            
         
            if(is_shom(words[i],words[j])):
                answer += 1
    print(answer)

def is_shom(str1, str2):

    dict1 = {}
    dict2 = {}
        

    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]

        if(char1 not in dict1.keys() and char2 not in dict2.keys()):
            dict1[char1] = char2
            dict2[char2] = char1
        elif(char1 in dict1.keys() and char2 not in dict2.keys()):
            if(dict1[char1] != char2):
                return False
            else:
                dict2[char2] = char1
        elif(char1 not in dict1.keys() and char2  in dict2.keys()):
            if(dict2[char2] != char1):
                return False
            else:
                dict1[char1] = char2
        else:
            if(dict1[char1]!=char2 or dict2[char2] != char1): return False

    return True

if __name__ == "__main__":
    solve()