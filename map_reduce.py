# Jack Lesemann jwl4vg


def mymap(func, lst):
    '''
    takes a single argument function and applies it to every item in list argument
    :param func:
    :param lst:
    :return:
    '''

    final_list = []

    for i in lst:
        new_i = func(i)
        final_list.append(new_i)
    return final_list


def myreduce(func, lst):
    '''
    takes a double argument function and applies function to first two items in list,
    then takes that result as the first argument of the function and uses the 3rd item in list as second argument.
    Continues this until the end of the list
    :param func:
    :param lst:
    :return:
    '''

    combined = lst[0]

    for i in range(1, len(lst)):
        combined = func(combined, lst[i])
    return combined
