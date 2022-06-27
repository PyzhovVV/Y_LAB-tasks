from tasks import find_all_numbers


primesL = [2, 3]
limit = 200
assert find_all_numbers.count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert find_all_numbers.count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert find_all_numbers.count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert find_all_numbers.count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert find_all_numbers.count_find_num(primesL, limit) == []