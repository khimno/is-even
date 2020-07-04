import is_odd as i

def is_even(num):
    if type(num) is int:
        return not i.valid(num)
    elif isinstance(num, str):
        return not i.valid(int(num))
    else:
        raise ValueError("Expected an int or an int as string")
