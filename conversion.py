def c2f(ftemp):
    """
    convert given celsius to fahrenheit
    :param ftemp:
    :return:
    """

    ctemp = (9 * (ftemp + 40) / 5) - 40

    return ctemp


def f2c(ctemp):
    """
    convert given fahrenheit to celsius
    :param ctemp:
    :return:
    """
    ftemp = (5 * (ctemp + 40) / 9) - 40

    return ftemp
