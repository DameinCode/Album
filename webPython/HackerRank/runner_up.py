# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_2 = -101
    max_1 = -101
    for i in range(0, len(arr)):
        if(arr[i] >= max_1):
            if (arr[i] != max_1):
                max_2 = max_1
            max_1 = arr[i]
        elif(arr[i] > max_2):
            max_2 = arr[i]
    print(max_2)