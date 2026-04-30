#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        list_result = []
        for i in range(len(my_list)):
            list_result.append(my_list[i] % 2 == 0)
        return list_result
