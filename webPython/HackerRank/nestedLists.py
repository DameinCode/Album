# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    result = {}
    min_2 = 101.0
    min_1 = 101.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in result:
            result[score].append(name)
        else:
            result[score] = [name]
    new_list = []
    for i in result:
        new_list.append([i, result[i]])
    new_list.sort()
    res = new_list[1][1]
    res.sort()
    print (*res, sep = '\n')