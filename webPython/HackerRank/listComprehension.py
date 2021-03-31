# https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    n = int(input())
    array = []
    for x in range(a+1):
        for y in range(b+1):
            for z in range(c+1):
                if(x+y+z != n):
                    array.append([x, y, z])
    
    print(array)