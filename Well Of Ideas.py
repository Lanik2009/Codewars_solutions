def well(x):
    if x.count('good') == 2 or x.count('good') == 1:
        return 'Publish!'
    elif x.count('good') > 2:
        return 'I smell a series!'
    elif x.count('good') == 0:
        return 'Fail!'