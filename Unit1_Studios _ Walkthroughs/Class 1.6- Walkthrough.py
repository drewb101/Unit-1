# Book's answer
#  def pos_or_neg(num):
#    if num > 0:
#        print('positive')
#    elif num < 0:
#        print('negative')


# def print_positives(the_ints):
#    for num in the_ints:
#        if num > 0:
#            print(num)


# def print_signed_integers(the_ints, the_sign):
#    if the_sign == 'positive':
#        for i in the_ints:
#            if i > 0:
#                print(i)
#    elif the_sign == 'negative':
#        for i in the_ints:
#            if i < 0:
#                print(i)

# Class walkthrough
def print_sign(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")


def print_positive(l):
    for i in l:
        if i > 0:
            print(i)


def print_negative(l):
    for i in l:
        if i < 0:
            print(i)


print_positive([2, -7, 8, 0, -2, -3, 9])


def print_ints(l, sign):
    if sign == "positive":
        print_positive(l)
    elif sign == "negative":
        print_negative(l)


print_sign(int(input("Please give a positive or negative number")))
