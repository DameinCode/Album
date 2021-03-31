# https://www.hackerrank.com/challenges/py-check-subset/problem?h_r=next-challenge&h_v=zen

tests = int(input())
result = []
for i in range(0, tests):
    len_a = int(input())
    A = list(map(int, input().split()))
    len_b = int(input())
    B = list(map(int, input().split()))
    result.append(set(A).issubset(set(B)))

for i in result:
    print(i) 