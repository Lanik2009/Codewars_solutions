def create_phone_number(n):
    n = ''.join([str(el) for el in n])
    return f"({''.join(n)[:3]}) {''.join(n)[3:6]}-{''.join(n)[6:]}"