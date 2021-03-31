def mini(a, b, c, d):
    ans1 = min(a, b)
    ans2 = min(c, d)
    return min(ans1, ans2)


a = [int(s) for s in input().split()]
print(mini(a[0], a[1], a[2], a[3]))