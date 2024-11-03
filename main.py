magenta = '\033[35m'
reset = '\033[0m'

def count_of_user_list():
    user_list = input('Enter the list: ')

    users_digits = 0
    users_letters = 0

    for char in user_list:
        if char.isalpha():
            users_letters += 1
        elif char.isdigit():
            users_digits += 1

    print(f'The number of digits in your string: {magenta}{users_digits}{reset}')
    print(f'The number of letters in your strings: {magenta}{users_letters}{reset}')

count_of_user_list()