def get_initials(fullname):
    name_list = fullname.split()
    init = ""
    for name in name_list:
        init = init + name[0]
    print(init)


def main():
    fullname = input("What is your full name?")

    print(get_initials)

if __name__ == '__main__':
    main()
