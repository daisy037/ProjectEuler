def Solution(num) :
    i = 1
    for k in range(1, num+1):
        if i % k > 0:
            for j in range(1, num+1):
                if (i * j) % k == 0:
                    i *= j
                    break
    return i


import time
start_time = time.time()
print(Solution(20))
print("--- %s seconds ---" % (time.time() - start_time))