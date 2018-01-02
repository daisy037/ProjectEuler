def main():
    pf = 1
    no = int(input("Enter Number :"))
    if no <= 1: print("No prime factor")
    tmp,i = no,2
    while tmp > 1:
        if tmp % i == 0 and isPrime(i):
            pf = i
            tmp //= i
            #print (tmp)
        i += 1
    print(pf)
def isPrime(no):
    for i in range(2,no//2+1):
        if(no%i == 0):
            return False
    return True

if __name__=='__main__' : main()
