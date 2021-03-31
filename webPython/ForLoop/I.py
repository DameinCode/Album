x = float(input())
import math
cnt = 1
if x == 1: 
    print(1)
    exit()
else:
    cnt = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if(x%i == 0):
            cnt += 1
if(int(math.sqrt(x))**2 == x):
    print((cnt*2)-1)
else:
    print(cnt*2)
