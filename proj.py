from math import log, sin, cos, fabs

NUM = 128

def even_max(value):

    def even_lhs():
        res_value = sin(value + NUM)
        if res_value == 0:
            return f"Error: devision zero"
        res_value = ((1-NUM) / res_value)
        if res_value < 0:
            return f"Error: log argument < 0"
        elif res_value == 0:
            return f"Error: log argument = 0"
        return log(res_value, 21)

    def even_rhs():
        return fabs(cos(value) / NUM)

    lhs = even_lhs()
    if isinstance(lhs, str):
        return lhs
    else:
        return max(lhs, even_rhs())

def odd_min(value):
    
    def odd_lhs():
        res_value = cos(value - NUM)
        if res_value == 0:
            return f"Error: devision zero"
        res_value = ((1-NUM) / res_value)
        if res_value < 0:
            return f"Error: log argument < 0"
        elif res_value == 0:
            return f"Error: log argument = 0"
        return log(res_value, 21)

    def odd_rhs():
        return sin(value) / NUM
    
    lhs = odd_lhs()
    if isinstance(lhs, str):
        return lhs
    else:
        return min(lhs, odd_rhs())

def table_former(init_val, fin_val, step):
    result_tab = open('result_tab.txt', 'w')
    
    str_step = str(step)
    if step%1 == 0:
        dec_places = 0
    elif str_step.find('.') != -1:
        dec_places = len(str_step.split('.')[1])
    else:
        dec_places = 5
    
    counter = 1

    print(f'{"Number":<10}{"Value":<{dec_places + 10}}{"Result":<40}')
    print(f'{"Number":<10}{"Value":<{dec_places + 10}}{"Result":<40}',
                                                        file=result_tab)

    while init_val <= fin_val:
        if (counter%2 == 0):
            result = even_max(init_val)
        else:
            result = odd_min(init_val)
        print(f'{counter:<10}{init_val:<{dec_places + 10}.{dec_places}f}{result:<40}')
        print(f'{counter:<10}{init_val:<{dec_places + 10}.{dec_places}f}{result:<40}',
                                                                        file=result_tab)
        counter, init_val = counter + 1, init_val + step

    result_tab.close()  

def main():
    while True:    
        try:
            initial = float(input("Input initial value: "))
            final = float(input("Input final value: "))
            if initial >= final:
                raise ValueError("initial value >= final value")
            step = float(input("Input sequence step: "))
            if step <= 0:
                raise ValueError("step value <= 0")
            break
            
        except Exception as excpt:
            print("Error: " + excpt.args[0], end='\n\n')

    table_former(initial, final, step)

if __name__ == "__main__":
    main()