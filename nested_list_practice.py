dict_grades = {}
dict_weights = {}
dict_total = {}


def assignment(kind, grade, weight=1):
    # Stores a running total and cumulative weight for each supplied grade type (kind).

    global dict_grades
    global dict_weights
    global dict_total

    total_grades = 0
    total_weight = 0

    if kind in dict_grades.keys():
        dict_grades[kind].append(grade * weight)
        dict_weights[kind].append(weight)

    else:
        dict_grades[kind] = [grade * weight]
        dict_weights[kind] = [weight]

    for g in dict_grades[kind]:
        total_grades += g
        print(g)
    for w in dict_weights[kind]:
        total_weight += w
        print(w)
    dict_total[kind] = total_grades / total_weight

    print(dict_grades, dict_weights, dict_total)


def total(proportions):
    """
    Given a dict with keys as types of assignments and values as ratios of
    overall grade this type applies to, returns the cumulative grade so far
    based on this set of proportions.
    """

    final_grade = 0

    for kind in dict_total.keys():
        if kind in proportions.keys():
            final_grade += (dict_total[kind] * proportions[kind])
        else:
            continue

    return final_grade


syllabus = {
    'exam': 0.5,
    'hw': 0.4,
    'lab': 0.1,
}

print(total(syllabus))
assignment('exam', 83)
assignment('exam', 88)
assignment('exam', 91, 2)
print(total(syllabus))
assignment('hw', 100)
assignment('hw', 100)
assignment('hw', 70)
assignment('hw', 0)
assignment('hw', 100, 4)
assignment('hw', 50)
assignment('lab', 90)
print(total(syllabus))
assignment('extra', 300)
print(total(syllabus))
