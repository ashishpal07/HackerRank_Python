#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    L = student_marks[query_name]
    s = sum(L)/len(L)
    print('%.2f' %s)
    
