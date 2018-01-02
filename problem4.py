def isPalindrome(no):
    tmp = no
    rev = 0
    while no > 0 :
        rem = no%10
        rev = rev*10 +rem
        no //= 10
    if(rev == tmp):
        return True
    else :
        return False

def main():
    pal = 0
    i = 999
    while i >= 100:
        j = 999
        while j >= i:
            if (i*j < pal):
                break
            if(isPalindrome(i*j)):
                pal = i * j
            j -= 1
        i -= 1
    print ("palindrome(3*3) : ",pal)


if __name__=='__main__' : main()