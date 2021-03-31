n = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    if(A[i] > A[i-1]):
        cnt += 1
print(cnt)