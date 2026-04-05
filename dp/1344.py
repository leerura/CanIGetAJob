import sys
import math

input = sys.stdin.readline

def solve():
    a = int(input().strip())/100
    b = int(input().strip())/100
    #최대 16골을 넣을 수 있음 그럼 2,3,5,7,11,13 골을 넣을 확률...?

    a_prob = [0] * 19
    b_prob = [0] * 19

    for i in range(19):
        a_prob[i] = math.comb(18,i)*(a**i)*((1-a)**(18-i))
        b_prob[i] = math.comb(18,i)*(b**i)*((1-b)**(18-i))

    primes = [2,3,5,7,11,13,17]
    

    no_prime_a = 0
    no_prime_b = 0

    for i in range(19):
        if(i not in primes):
            no_prime_a +=a_prob[i]
            no_prime_b +=b_prob[i]




    print(1-no_prime_a*no_prime_b)



    

if __name__=="__main__":
    solve()