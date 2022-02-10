def get_count(input_str):
    a = 0
    vowel = 'aieou'
    for v in vowel:
        a += input_str.count(v)
    return a