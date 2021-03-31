# a = [int(s) for s in input().split()]
n = int(input())
A = list(map(int, input().split()))

print(' '.join(map(str, reversed(A))))