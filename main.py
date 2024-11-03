# В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы,
# сосчитать количество отрицательных элементов, сосчитать количество положительных элементов,
# сосчитать количество нулей. Результаты выводятся на экран.

def calculating_numbers():
    numbers_list = [3, 74, 0, 12, -4, 8, 0, -7, 5, 12, 34, 87, -7, 0, 0, 6, 0, 32, 76, 88, -5, 0, -0,75]
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

    for number in numbers_list:
        if number < my_min_number:
            my_min_number = number

        elif number > my_max_number:
            my_max_number = number

    print(f'Min: {my_min_number}, Max: {my_max_number}, Zero: {count_of_zero}, Positive: {count_of_positive_num}, Negative: {count_of_negative_num}')

calculating_numbers()