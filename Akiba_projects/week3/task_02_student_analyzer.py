
students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]


def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError('Score must be between 0 and 100.')


def calculate_grade(score):
    validate_score(score)

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def calculate_average(students):
    if len(students) == 0:
        raise ValueError('There is no student to analyze.')

    total = 0

    for student in students:
        validate_score(student['score'])
        total += student['score']

    average = total / len(students)
    return average


def highest_lowest_score(students):
    if len(students) == 0:
        raise ValueError('There is no student to analyze.')

    highest = students[0]['score']
    lowest = students[0]['score']

    for student in students:
        validate_score(student['score'])

        if student['score'] > highest:
            highest = student['score']

        if student['score'] < lowest:
            lowest = student['score']

    return highest, lowest


def pass_fail(students):
    pass_count = 0
    fail_count = 0

    for student in students:
        validate_score(student['score'])

        if student['score'] >= 50:
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count


def students_above_average(students, average):
    above_average = []

    for student in students:
        if student['score'] > average:
            above_average.append(student)

    return above_average


def generate_report(students):
    if len(students) == 0:
        raise ValueError('There is no student to analyze.')

    average = calculate_average(students)
    highest, lowest = highest_lowest_score(students)
    pass_count, fail_count = pass_fail(students)

    print('          STUDENT PERFORMANCE REPORT   ')

    for student in students:
        grade = calculate_grade(student['score'])

        if student['score'] >= 50:
            status = 'Passed'
        else:
            status = 'Failed'

        print('Name:', student['name'])
        print('Score:', student['score'])
        print('Grade:', grade)
        print('Status:', status)
        print('--------------------------------')

    above_average = students_above_average(students, average)

    print('Class Average:', round(average, 2))
    print('Highest Score:', highest)
    print('Lowest Score:', lowest)
    print('Students Passed:', pass_count)
    print('Students Failed:', fail_count)

    print('      -------------    ')
    print('Students Above Class Average:')
    for student in above_average:
        print(student['name'], '-', student['score'])


generate_report(students)
