sum,a1,a2 = 2,1,2
n = int(input("Enter limit : "))
while True :
    tmp = a1+a2
    a2 = a2+tmp
    a1 = tmp
    if a1 > n or a2 > n :
        break
    if a1 % 2 == 0 :
        sum += a1
    if a2 % 2 == 0 :
        sum += a2
print (sum)