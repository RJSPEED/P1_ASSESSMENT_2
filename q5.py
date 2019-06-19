
def zero_sort(the_list):
    for i in the_list:
        if i == 0:
            the_list.append(i)
            the_list.remove(i)

    print(the_list)

the_list = [1, 0, 7, 2, 0, 3, 9, 0, 4]

zero_sort(the_list)

