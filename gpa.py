gpatrack = 0
credittrack = 0


def add_course(grade, course=3):
    """
    keeps value total in gpatrack and credittrack
    :param grade:
    :param course:
    :return:
    """
    global gpatrack
    global credittrack

    gpatrack = ((gpatrack * credittrack) + (grade * course)) / (credittrack + course)
    credittrack = credittrack + course



def gpa():
    """
    :return: running gpa
    """
    return gpatrack


def credit_total():
    """
    :return: running credit
    """
    return credittrack
