#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except(ZeroDivisionError, TypeError):
            if type(my_list_1[1]) not in (int, float) or type(my_list_2[i]) not in (int, float):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            else:
                print("out of range")
                result = 0
        finally:
            result_list.append(result)

    return result_list
