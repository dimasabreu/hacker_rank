if __name__ == '__main__':
    
    """ The provided code stub will read in a dictionary containing
    key/value pairs of name:[marks] for a list of students.
    Print the average of the marks array for the student name provided,
    showing 2 places after the decimal."""

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for x in student_marks.keys():
        if x == query_name:
            media = float(sum(student_marks.get(query_name))) / 3
            print('%.2f' % (media))
