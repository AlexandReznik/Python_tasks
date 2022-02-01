tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(teachers, clas):
    i = 0
    j = 0
    while i != len(clas):
        if j == clas[-1]:
            yield (None, clas[j])
            i += 1
            j += 1
        elif i == teachers[-1]:
            yield (teachers[i], None)
        else:
            yield (teachers[i], clas[j])
            i += 1
            j += 1
    return 0


generator = check_gen(tutors, classes)
for _ in range(len(tutors)):
    print(next(generator))

