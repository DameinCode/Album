#  https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=next-challenge&h_v=zen
def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)