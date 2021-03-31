# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0.0 
    for name in student_marks:
        if(query_name == name):
            for scores in student_marks[name]:
                result += scores
            break
    
    print("{:.2f}".format(result/3))