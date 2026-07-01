if __name__ == '__main__':
    result = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    lowest_score = min([s[1] for s in students])
    nd_lowest_score = min(s[1] for s in students if s[1] != lowest_score)
    for student in students:
        if student[1] == nd_lowest_score:
            result.append(student[0])
    result.sort()
    for student in result:
        print(student)
