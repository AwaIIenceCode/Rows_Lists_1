def count_word ():
    user_list = input('Enter the string: ')
    user_word = input('Enter the word: ')

    count_user_word = user_list.count(user_word)

    print(count_user_word)

count_word()

#the count method depends on the case of the first letter, so to make it handle this,
#you must write: count_user_word = user_list.lower().count(user_word.lower())