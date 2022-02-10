def sum_two_smallest_numbers(numbers):
    s = sorted(numbers)
    s1 = s[0:2]
    return sum(s1)