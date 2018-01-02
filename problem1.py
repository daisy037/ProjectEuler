sum = 0
n = int(input("Enter limit : "))
print (n)
for i in range (1,n) :
	if ((i % 3 == 0) or (i % 5 == 0)):sum += i
print("sum = " +str(sum))

