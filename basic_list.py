"""
Program:  basic_list.py
author:  Lisa Kilmer
Program makes a list with the make_list function.  Is supposed to have
a get_input function that I haven't figured where to put it. changes input
to an int after the input and adds to list or if not an int raise a
ValueError.  Return the list

"""

list = []


def make_list(list):
    for i in range(0, 3):
        num = input("Enter a number: ")
        num = int(num)
        list.append(num)
    if type(num) != int:
        raise ValueError('not a number')

    return list


if __name__ == '__main__':
    list = make_list(list)
    print(list)







