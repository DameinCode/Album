n = int(input())
A = list(map(int, input().split()))
for i in range(1, n):
    if(A[i] > 0 and A[i-1] > 0 or A[i] < 0 and A[i-1] < 0):
        print('YES')
        exit()
print('NO')