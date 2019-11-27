bmr = 0


def st_jeor(mass, height, age, sex):
    """
    take mass, height, age, sex and compute basal metabolic rate
    :param mass:
    :param height:
    :param age:
    :param sex:
    :return:
    """
    global bmr

    if sex in ['female', 'Female', 'FEMALE', 'f', 'F']:
        bmr = ((10 * mass) + (6.25 * height) - (5 * age)) - 161
    elif sex in ['male', 'Male', 'MALE', 'm', 'M']:
        bmr = ((10 * mass) + (6.25 * height) - (5 * age)) + 5
    return bmr
