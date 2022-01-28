from math import log, sin, cos, fabs

NUM = 128

def even_lhs(value):
        res_value = sin(value + NUM)
        if res_value == 0:
            return f"Error: devision zero"
       
        res_value = ((1-NUM) / res_value)
        if res_value < 0:
            return f"Error: log argument < 0"
        elif res_value == 0:
            return f"Error: log argument = 0"
        return log(res_value, 21)

def even_rhs(value):
    return fabs(cos(value) / NUM)

def even_max(value):
    lhs = even_lhs(value)
    if isinstance(lhs, str):
        return lhs
    else:
        return max(lhs, even_rhs(value))

def odd_lhs(value):
    res_value = cos(value - NUM)
    if res_value == 0:
        return f"Error: devision zero"
    res_value = ((1-NUM) / res_value)
    if res_value < 0:
        return f"Error: log argument < 0"
    elif res_value == 0:
        return f"Error: log argument = 0"
    return log(res_value, 21)

def odd_rhs(value):
    return sin(value) / NUM

def odd_min(value):
    lhs = odd_lhs(value)
    if isinstance(lhs, str):
        return lhs
    else:
        return min(lhs, odd_rhs(value))

def table_former(init_val, fin_val, step):
    def dec_placer():
        str_step = str(step)
        if step%1 == 0:
            return 0
        elif str_step.find('.') != -1:
            return len(str_step.split('.')[1])
        else:
            return 5

    with open('result_tab.txt', 'w') as result_tab:
        dec_places = dec_placer()
        
        counter = 1
    
        print('-' * (54 + dec_places))
        print(f'|{"Number":^10}|{"Value":^{dec_places + 10}}|{"Result":^30}|')
        print('-' * (54 + dec_places))
        print('-' * (54+dec_places), file=result_tab)
        print(f'|{"Number":^10}|{"Value":^{dec_places + 10}}|{"Result":^30}|',
                                                            file=result_tab)
        print('-' * (54+dec_places), file=result_tab)

        while init_val <= fin_val:
            if (counter%2 == 0):
                result = even_max(init_val)
            else:
                result = odd_min(init_val)
            print(f'|{counter:>10}|{init_val:>{dec_places + 10}.{dec_places}f}|{result:>30}|')
            print(f'|{counter:>10}|{init_val:>{dec_places + 10}.{dec_places}f}|{result:>30}|',
                                                                            file=result_tab)
            counter += 1
            init_val += step 

        print('-' * (54 + dec_places))
        print('-' * (54+dec_places), file=result_tab)

def main():
    while True:    
        try:
            initial = float(input("Input initial value: "))
            final = float(input("Input final value: "))
            if initial >= final:
                raise ValueError("initial value >= final value")
            step = float(input("Input sequence step: "))
            if step == 0:
                raise ValueError("step value = 0")
            break
        except Exception as excpt:
            print("Error: " + excpt.args[0], end='\n\n')

    table_former(initial, final, step)

if __name__ == "__main__":
    main()