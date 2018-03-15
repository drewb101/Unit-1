def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    



def main():
    fullname = input("What is your full name?")
    inits = get_intitials(fullname)
    print("The initials of", "'"+fullname+"'", "are", inits)
# => prints "The initials of 'Ozzie Smith' are OS"

if __name__ == '__main__':
    main()