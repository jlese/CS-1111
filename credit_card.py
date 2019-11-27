#jwl4vg Jack Lesemann


def check(number):
    '''
    take a number as int, convert it to a string and reverse it. Start with the right most (now the first number) in the
    string and add every other number. Take left over numbers, double them, then add the digits (10 = 1+0). Combine the
    sum of the two sets, return True if the sum is divisible by 10.
    :param number:
    :return:
    '''
    sum_list = 0
    number = str(number)

    reverse_number = number[::-1]

    for i in range(0, len(reverse_number), 2):
        sum_list += int(reverse_number[i])

    double_rest_string = ''
    double_rest_sum = 0

    for i in range(1, len(reverse_number), 2):
        double_rest = int(reverse_number[i]) * 2
        double_rest_string += str(double_rest)

    for q in range(0, len(double_rest_string)):
        double_rest_sum += int(double_rest_string[q])

    final_sum = str(sum_list + double_rest_sum)

    if final_sum[-1] == "0":
        result = True
    else:
        result = False

    return result




