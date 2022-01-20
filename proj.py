from math import log, sin, cos, fabs

NUM = 128

def even_lhs(value):
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

def even_rhs(value):
    return fabs(cos(value) / NUM)

def odd_lhs(value):
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

def odd_rhs(value):
    return sin(value) / NUM

def min_max_evaluator(eval_lhs, eval_rhs, value):
    lhs = eval_lhs(value)
    if isinstance(lhs, str):
        return lhs
    else:
        return max(lhs, eval_rhs(value))

def table_former(init_val, fin_val, step):
    result_tab = open('result_tab.txt', 'w')
    counter = 1
    while init_val <= fin_val:
        if (counter%2 == 0):
            result = min_max_evaluator(even_lhs,
                                    even_rhs, init_val)
        else:
            result =min_max_evaluator(odd_lhs,
                            odd_rhs, init_val)
        print(f'{counter:<10}{init_val:<10}{result:<40}')
        print(f'{counter:<10}{init_val:<10}{result:<40}',
                                        file=result_tab)
        counter += 1
        init_val += step
    result_tab.close()  

def main():
    try:
        initial = float(input("Input initial value: "))
        final = float(input("Input final value: "))
        if initial > final:
            raise ValueError("Error in main: initial value > final value")
        step = float(input("Input sequence step: "))
        if step == 0:
            raise ValueError("Error in main: step value = 0")
    except ValueError:
        pass

    table_former(initial, final, step)


if __name__ == "__main__":
    __main__()