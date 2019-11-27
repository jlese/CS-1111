ctemp = float(input("What is the temperature in Celsius? "))


def celsius_convert():
    """
    convert given celsius to fahrenheit
    """
    global ctemp
    ctemp = (9 * (ctemp + 40) / 5) - 40

    return ctemp


celsius = celsius_convert()

print("It is " + str(celsius) + " degrees Fahrenheit")

"""
fheit = (9 * (ctemp + 40) / 5) - 40

print(fheit)
"""

# Jack Lesemann jwl4vg
