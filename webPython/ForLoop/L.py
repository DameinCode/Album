n = input()
cnt = 0
ans = 0
for i in range(len(n)-1, -1, -1):
    ans += int(n[i])* (2**cnt)
    cnt += 1

print(ans)