def power(n, po):
    if po == 0:
        return 1
    else:
        return n * power(n, po - 1)

n, po = input().split()
print(str(int((power(float(n), int(po))))))