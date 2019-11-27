# jwl4vg Jack Lesemann
grade_total = {}
weight_lists = {}
current_total = {}


def assignment(kind, grade, weight=1):
    '''
    adds scores and weights to a running total under their individual assignment type. keeps a current total of the
    grades divided by the weights
    :param kind:
    :param grade:
    :param weight:
    :return:
    '''

    global grade_total
    global weight_lists
    global current_total

    if kind in grade_total:
        grade_total[kind] += grade * weight
        weight_lists[kind] += weight
    else:
        grade_total[kind] = grade * weight
        weight_lists[kind] = weight

    current_total[kind] = grade_total[kind] / weight_lists[kind]


def total(proportions):
    '''
    takes the proportion provided and returns current final score
    :param proportions:
    :return:
    '''

    final_grade = 0

    for kind in current_total:
        if kind in proportions:
            final_grade += (current_total[kind] * proportions[kind])
        else:
            continue

    return final_grade





















