# Gavin Howard
# List Ops Methods
# 2/10/2020

import collections
from listops import user_values

user_values.sort()
print("Here are your values in ascending order: " + str(user_values))


def largest():
    print("Here is the largest number in your list: ", user_values[4])


def smallest():
    print("Here is the smallest number in your list: ", user_values[0])


def median():
    print("Here is the median of the numbers you provided: ", user_values[2])


def sum_values(user_values):
    sum = 0
    for value in user_values:
        sum += value
    return sum


def product_values(user_values):
    product = 0
    for value in user_values:
        product *= value
    return product


def mean_values(user_values):
    sum = 0
    for value in user_values:
        sum += value
    mean = sum / len(user_values)
    return mean


def strip_evens(user_values):
    for value in user_values:
        if value % 2 == 0:
            user_values.remove(value)
    return user_values


def strip_odds(user_values):
    for value in user_values:
        if value % 2 != 0:
            user_values.remove(value)
    return user_values


def ask():
    print("Enter a number to see if it's in the list!")
    ask_num = int(input('> '))
    if ask_num in user_values:
        print(ask_num, " is in the list!")
    else:
        print(ask_num, " is not in the list!")


def duplicate_removal(user_values):
    return set(user_values)


def mode(user_values):
    data = collections.Counter(user_values)
    data_list = dict(data)
    print("Here is your list, and how many times each number was entered: ", data_list)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(user_values):
        print("No mode in the list")
    else:
        print("The Mode of the list is : " + ', '.join(map(str, mode_val)))


print("The sum of your list is: ", sum_values(user_values))
print(largest())
print(smallest())
print(median())
print("The product of your list is: ", product_values(user_values))
print("The mean of your list is: ", mean_values(user_values))
mode(user_values)
ask()
print("Here is your list without even numbers: ", strip_evens(user_values))
print("Here is your list without odd numbers: ", strip_odds(user_values))
print("Here is your list without duplicates: ", duplicate_removal(user_values))

