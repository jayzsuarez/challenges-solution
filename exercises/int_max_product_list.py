import itertools

'''
Problem: Given a list of integers, find the highest product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
'''


def list_of_ints(data_list):
    if len(data_list) >= 3:
        product_list = []
        subset = {p for p in itertools.product(data_list, repeat=3)}
        for items in subset:
            product_list.append(get_product(items))
        print(f"The max possible product of list {data_list} is {get_max(product_list)}.")
    else:
        print(f"The list of {data_list} should have at least 3 integers!")


def get_product(data_list):
    result = 1
    for int_value in data_list:
        result = result * int_value
    return result


def get_max(data_list):
    return max(data_list)


if __name__ == '__main__':
    list_of_ints([-10, -10, 1, 3, 2])
    list_of_ints([1, 3])
