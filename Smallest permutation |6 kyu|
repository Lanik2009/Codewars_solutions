def min_permutation(n):
    if n == 0:
        return 0
    s = ''.join(sorted(str(n)))
    c = s.count('0')
    s = s.replace('0', '')
    if s[0] != '-':
        s = s[0] + '0' * c + s[1:]
    else:
        s = s[:2] + '0' * c + s[2:]
    return int(s)
    print(s)
