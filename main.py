#var1

def my_list():
    user_list = [input('Type in the string: ')]

    reversed_user_list = user_list[0][::-1]

    print(f'Your result: {reversed_user_list}')

my_list()

#var2 without using a list

def my_list():
    user_string = input('Type in the string: ')
    reversed_string = user_string[::-1]
    print(f'Your result: {reversed_string}')

my_list()
