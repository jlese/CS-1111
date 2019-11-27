ma = 0



def mean(a, b, c):
    """
    calculate mean of 3 values
    :param a:
    :param b:
    :param c:
    :return:
    """
    mn = (a + b + c) / 3
    return mn


def median(a, b, c):
    """
    calculate median of 3 values
    :param a:
    :param b:
    :param c:
    :return:
    """

    if a > b:
        if a > c:
            if c > b:
                return c
            else:
                return b
        else:
            return a
    else:
        if b > c:
            if a > c:
                return a
            else:
                return c
        else:
            return b



def rms(a, b, c):
    """
    calculate root mean square of 3 values
    :param a:
    :param b:
    :param c:
    :return:
    """
    a_sqr = a ** 2
    b_sqr = b ** 2
    c_sqr = c ** 2

    mn_sqr = mean(a_sqr, b_sqr, c_sqr)

    root_mn_sqr = mn_sqr ** .5

    return root_mn_sqr


def middle_average(a, b, c):
    """
    calculate mean of the three return values from previous functions
    :param a:
    :param b:
    :param c:
    :return:
    """
    global ma
    mn1 = mean(a, b, c)
    md1 = median(a, b, c)
    rms1 = rms(a, b, c)

    ma = median(mn1, md1, rms1)

    return ma



# jack lesemann jwl4vg
