from helpers import alphabet_position, rotate_character

def encrypt(text,key):
    cipher = ''
    l = len(key)
    idx = 0
    for i in text:
        if i.isalpha():
            cipher += rotate_character(i,alphabet_position(key[idx])) 
            idx = (idx+1)%l
        else:
            cipher += i
    return cipher


def main():
    text = raw_input("Type a message: \n")  
    key = raw_input("Encryption key: \n")
    print(encrypt(text,key))

if __name__ == '__main__':
    main()