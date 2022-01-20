from math import log, sin, cos, fabs

NUM = 128

def even_rhs(value):
    '''even_rhs test
    >>> even_rhs(0)
    'Error in even_rhs: log argument < 0'
    >>> even_rhs(-128)
    'Error in even_rhs: devision zero'
    '''
    res_value = sin(value + NUM)
    if res_value == 0:
        return f"Error in even_rhs: devision zero"
    res_value = ((1-NUM) / res_value)
    if res_value < 0:
        return f"Error in even_rhs: log argument < 0"
    return log(res_value, 21)

def even_lhs(value):
    return fabs(cos(value) / NUM)

def odd_rhs(value):
    '''odd_rhs test
    >>> odd_rhs(129)
    'Error in odd_rhs: log argument < 0'
    >>> odd_rhs(128)
    'Error in odd_rhs: log argument < 0'
    '''
    res_value = cos(value - NUM)
    if res_value == 0:
        return f"Error in odd_rhs: devision zero"
    res_value = ((1-NUM) / res_value)
    if res_value < 0:
        return f"Error in odd_rhs: log argument < 0"
    return log(res_value, 21)

def odd_lhs(value):
    return sin(x) / NUM











if __name__ == "__main__":
    func()