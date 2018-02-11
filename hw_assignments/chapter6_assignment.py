# A year is a leap year if it is divisible by 4, unless it is a century that is not divisible by 400.

# For example:

#   1956 is a leap year because 1956 is divisible by 4.
#   1957 is not a leap year, because it is not divisible by 4.
#   1900 is not a leap year, despite the fact that it is divisible by 4, because 1900 is a century and 1900 is not
#       divisible by 400.
#   1600 is a leap year, because 1600 is divisible by 4 and 1600 is divisible by 400
#
#
# Write a function is_leap that takes a year as a parameter and returns True if the year is a leap year, False
#   otherwise.
def is_leap(year):
    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
# Below is a set of tests so you can check if your code is correct.
# Do not copy this part into Vocareum.
from test import testEqual

testEqual(is_leap(1944), True)
testEqual(is_leap(2011), False)
testEqual(is_leap(1986), False)
testEqual(is_leap(1956), True)
testEqual(is_leap(1957), False)
testEqual(is_leap(1800), False)
testEqual(is_leap(1900), False)
testEqual(is_leap(1600), True)
testEqual(is_leap(2056), True)
