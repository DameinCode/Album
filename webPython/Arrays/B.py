n = int(input())
A = list(map(int, input().split()))

for i in range(0, n):
    if(A[i]%2 == 0):
        print(A[i], end = ' ')