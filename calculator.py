# Jack Lesemann jwl4vg

def binop(string):
    '''
    takes a string and extracts the two numbers and operator. it will then return the answer to the extracted expression
    :param string: two integers and +, -, /, or *
    :return: answer as float
    '''

    if "/" in string:
        string_strip = string.strip()

        location = string_strip.find("/")

        i = 0

        while i < location:
            i += 1

        num1 = int(string_strip[0:i])
        num2 = int(string_strip[i + 1:len(string_strip)])

        answer = num1 / num2

        return answer

    elif "*" in string:
        string_strip = string.strip()

        location = string_strip.find("*")

        i = 0

        while i < location:
            i += 1

        num1 = int(string_strip[0:i])
        num2 = int(string_strip[i + 1:len(string_strip)])

        answer = num1 * num2

        return answer

    elif "+" in string:
        string_strip = string.strip()

        location = string_strip.find("+")

        i = 0

        while i < location:
            i += 1

        num1 = int(string_strip[0:i])
        num2 = int(string_strip[i + 1:len(string_strip)])

        answer = num1 + num2

        return answer

    elif "-" in string:
        string_strip = string.strip()

        location = string_strip.find("-")

        i = 0

        while i < location:
            i += 1

        num1 = int(string_strip[0:i])
        num2 = int(string_strip[i + 1:len(string_strip)])

        answer = num1 - num2

        return answer
