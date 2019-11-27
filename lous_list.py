#Jack Lesemann jwl4vg

import urllib.request


def instructors(department):
    """
    reads in the data from the given department, iterates through rows and if professor is not already in list, appends
    professor name. returns list of instructors
    :param department:
    :return:
    """
    data = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + department).read().decode('utf-8').split('\n')
    instructor_list = []

    for line in data:
        row = line.strip().split("|")
        if row[0] == department:
            new_instructor = row[4]
            if new_instructor[-2] == '+':
                new_instructor = new_instructor[0:-2]
            if new_instructor not in instructor_list:
                instructor_list.append(new_instructor)

    instructor_list.sort()

    return instructor_list


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    """
    reads in the data from the given department, checks each class with given parameters, returns a list of lists of
    matching classes
    :param dept_name:
    :param has_seats_available:
    :param level:
    :param not_before:
    :param not_after:
    :return:
    """
    data = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + dept_name)

    class_list = []

    for course in data:
        row = course.decode("UTF-8").strip().split("|")
        if has_seats_available is True:
            if row[15] > row[16]:
                continue
        if level is not None:
            if str(level)[0] != row[1][0]:
                continue
        if not_before is not None:
            if int(row[12]) < not_before:
                continue
        if not_after is not None:
            if int(row[13]) > not_after:
                continue
        class_list.append(row)
    return class_list


