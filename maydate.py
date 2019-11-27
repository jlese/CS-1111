def creepy(age1, age2):
    """
    take two ages and return true if it is ok to date and false if not
    """
    age1 = age1 * 2 - 13

    return bool(age1 <= age2)


