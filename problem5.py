
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(n1,n2):
    masavi = 1
    flg = 0
    while True:
        i = 2
        while i < n1 or i < n2:
            if(n1 % i == 0 and n2 % i == 0):
                n1 = n1//i
                n2 = n2//i
                masavi *= i
                flg = 1
            i += 1
        if flg == 0:
            masavi = masavi*n1*n2
            break
        flg = 0
    return masavi


def lcm2(n1,n2):
    return (n1*n2)//gcd(n1,n2)


def main():
    #n = int(input("Eneter limit"))
    n = 20
    i = 1
    masavi = 1
    for i in range(2,n+1):
        masavi = lcm2(masavi,i)
    print("smallest positive number that is evenly divisible by all of the numbers from 1 to n :",masavi)

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))