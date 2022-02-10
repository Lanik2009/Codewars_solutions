def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<b+a)