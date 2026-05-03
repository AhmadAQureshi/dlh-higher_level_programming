#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = 0
    total_sum = 0

    for number, weight in my_list:
        total_weight += weight
        total_sum += number * weight

    return total_sum / total_weight
