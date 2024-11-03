#var_1

def count_symbol ():
    user_list = input('Enter the string: ')
    user_symbol = input('Enter the symbol: ')

    count_user_symbol = 0

    for symbol in user_list:
        if symbol == user_symbol:
            count_user_symbol += 1

    print(count_user_symbol)

count_symbol()

#var_2 with the method .count

def count_symbol():
    user_list = input('Enter the string: ')
    user_symbol = input('Enter the symbol: ')

    count_user_symbol = user_list.count(user_symbol)

    print(count_user_symbol)

count_symbol()
