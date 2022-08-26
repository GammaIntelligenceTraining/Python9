import itertools
#
# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Jack', 'John']
#
#
# # Will return all possible combinations where order does not matter
# result = itertools.combinations(letters, 2)
#
# for item in result:
#     print(item)
#
# # Will return all possible combinations where order does matter
# # Does not return doubled combinations like ['a', 'a']
# result = itertools.permutations(letters, 2)
#
# for item in result:
#     print(item)
#
# # Will return all possible combinations including repeating symbols
# result = itertools.product(numbers, repeat=4)
#
# for item in result:
#     print(item)
#
#
# # Will return all possible combinations including repeating symbols order doesn't matter
# result = itertools.combinations_with_replacement(numbers, 4)
#
# for item in result:
#     print(item)
#
#
# # Combine all lists
#
# # Chains list into one list
# combined = itertools.chain(letters, numbers, names)
#
# for item in combined:
#     print(item)
#
# # Takes two arguments (iterable, stop_point)
# combined = itertools.islice(range(10), 5)
#
# # Or three values (iterable, start_point, stop_point)
# combined = itertools.islice(range(10), 1, 5)
#
# # Or four values (iterable, start_point, stop_point, step)
# combined = itertools.islice(range(10), 1, 5, 2)
#
# for item in combined:
#     print(item)

# Sample of use
with open('demo_log.txt', 'r', encoding='utf8') as file:
    log_header = itertools.islice(file, 3)
    log_header2 = itertools.islice(file, 3)


    for line in log_header:
        print(line, end='')

    for line in log_header2:
        print(line, end='')
