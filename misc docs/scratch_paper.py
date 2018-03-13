def num_digits(text):
    total = 0
    for char in text:
        if char in string.digits == True:
            total = total + 1
    return total

def main():
    print(num_digits("y0l0 my br0s"))
    