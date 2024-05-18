positions = ['LW', 'C', 'RW', 'LD', 'RD', 'GK']


def do_to_list(working_list, working_fn, desc):
    value = working_fn(working_list)
    return f'{desc} {value}'


def last_elem_in_list(working_list):
    return working_list[-2]


do_to_list(positions, last_elem_in_list, " Second to last element in list:")
do_to_list([2, 3, 7, 1.3, 5], lambda x: 3 * x[0], "First element in list multiplied by 3:")

print()