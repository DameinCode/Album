n = int(input())
i = 1
while i <= n:
    if i == n:
        print('YES')
        exit()
    i *= 2
print('NO')