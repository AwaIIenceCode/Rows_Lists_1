magenta = '\033[35m'
reset = '\033[0m'

def calculating_numbers():
    numbers_list = [3, 74, 0, 12, -4, 8, 0, -7, 5, 12, 34, 87, -7, 0, 0, 6, 0, 32, 76, 88, -5, 0, -0.75, -11]
    count_of_negative_num = 0
    count_of_positive_num = 0
    count_of_zero = 0
    my_min_number = numbers_list[0]
    my_max_number = numbers_list[0]

    for number in numbers_list:
        if number > 0:
            count_of_positive_num += 1
        elif number < 0:
            count_of_negative_num += 1
        else:
            count_of_zero += 1


        if number < my_min_number:
            my_min_number = number

        elif number > my_max_number:
            my_max_number = number

    print(f'Your min: {magenta}{my_min_number}{reset}\nYour max: {magenta}{my_max_number}{reset}\nNumber of zeroes: {magenta}{count_of_zero}{reset}')
    print(f'Number of pozitive: {magenta}{count_of_positive_num}{reset}\nNumber of negative: {magenta}{count_of_negative_num}{reset}')

calculating_numbers()