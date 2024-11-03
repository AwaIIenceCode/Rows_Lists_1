def replace_word_in_string():
    user_string = input('Enter the strings: ')
    found_word = input('Enter the found word: ')
    insert_word = input('Enter the insert word: ')

    result_string = user_string.replace(found_word, insert_word)
    print(result_string)

replace_word_in_string()
