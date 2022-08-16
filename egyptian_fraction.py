import math

def egyptian_fraction(numerator, denominator):
    """
    Finds the egyptian fraction denominators
    :param numerator: Numerator of the fraction
    :param denominator: Denominator of the fraction
    :return: A list of denominators of the egyptian fraction
    """

    # A List to store denominator
    lst_denominator = []

    # While loop runs until fraction becomes 0 i.e,
    # numerator becomes 0
    while numerator != 0:
        # taking ceiling
        x = math.ceil(denominator / numerator)

        # storing value in lst_denominator list
        lst_denominator.append(x)

        # updating new numerator and denominator
        numerator = x * numerator - denominator
        denominator = denominator * x

    return lst_denominator


# Driver code to test above function
if __name__ == '__main__':

    print(egyptian_fraction(6, 14))
    print(egyptian_fraction(2, 3))
