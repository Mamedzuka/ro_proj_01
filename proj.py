from math import log, sin, cos, fabs

NUM = 128

#Функция, считающая выражение для чётных номеров
#Внутри содержит две функции, отвечающие за lhs -
#левый и rhs - правый аргументы в функции max
#Принимает значение value - значение из диапазона
def even_max(value):
    #Левый аргумент функции max
    #Формальных параметров не имеет
    #Работает с value из внешней функции
    #Сделано для невозможности изменения 
    #значения value в ходе работы функции
    def even_lhs():
        #1) вычисляется значение знаменателя в логарифме
        #Если данное значение равно нулю - функция
        #возвращает код ошибки, передаваемый в таблицу
        res_value = sin(value + NUM)
        if res_value == 0:
            return f"Even_max error: devision zero"
        #2) вычисляется значение аргумента логарифма
        #Если данное значение равно нулю или меньше нуля 
        #функция возвращает код ошибки, передаваемый в таблицу
        res_value = ((1-NUM) / res_value)
        if res_value < 0:
            return f"Even_max error: log argument < 0"
        elif res_value == 0:
            return f"Even_max error: log argument = 0"
        #3) ошибки не убнаружены - вычисляем значение логарифма
        #возвращаем его
        return log(res_value, 21)

    #Правый аргумент функции max
    #Формальных параметров не имеет
    #Работает с value из внешней функции
    #Сделано для невозможности изменения 
    #значения value в ходе работы функции
    def even_rhs():
        #Возвращаем значения правого аргумента функции max
        return fabs(cos(value) / NUM)

    #вычисляем значение левого аргумента функции max - функции even_lhs()
    #если данное значение - строка, то это код ошибки - возвращаем данный код
    #если данное значение - число, то передаём его в функцию max вместе с 
    #правым аргументом функции max - функцией even_rhs()
    #возвращаем значение функции max
    lhs = even_lhs()
    if isinstance(lhs, str):
        return lhs
    else:
        return max(lhs, even_rhs())

#Функция, считающая выражение для нечётных номеров
#Внутри содержит две функции, отвечающие за lhs -
#левый и rhs - правый аргументы в функции max
def odd_min(value):
    #Левый аргумент функции max
    #Формальных параметров не имеет
    #Работает с value из внешней функции
    #Сделано для невозможности изменения 
    #значения value в ходе работы функции
    def odd_lhs():
        #1) вычисляется значение знаменателя в логарифме
        #Если данное значение равно нулю - функция
        #возвращает код ошибки, передаваемый в таблицу
        res_value = cos(value - NUM)
        if res_value == 0:
            return f"Odd_min error: devision zero"
        #2) вычисляется значение аргумента логарифма
        #Если данное значение равно нулю или меньше нуля 
        #функция возвращает код ошибки, передаваемый в таблицу
        res_value = ((1-NUM) / res_value)
        if res_value < 0:
            return f"Odd_min error: log argument < 0"
        elif res_value == 0:
            return f"Odd_min error: log argument = 0"
        #3) ошибки не убнаружены - вычисляем значение логарифма
        #возвращаем его
        return log(res_value, 21)

    #Правый аргумент функции max
    #Формальных параметров не имеет
    #Работает с value из внешней функции
    #Сделано для невозможности изменения 
    #значения value в ходе работы функции
    def odd_rhs():
        #Возвращаем значения правого аргумента функции min
        return sin(value) / NUM

    #вычисляем значение левого аргумента функции max - функции odd_lhs()
    #если данное значение - строка, то это код ошибки - возвращаем данный код
    #если данное значение - число, то передаём его в функцию max вместе с 
    #правым аргументом функции min - функцией odd_rhs()
    #возвращаем значение функции min
    lhs = odd_lhs()
    if isinstance(lhs, str):
        return lhs
    else:
        return min(lhs, odd_rhs())

#Функция, формирующая таблицу с итоговыми значениями
#Три формальных параметра
#inin_value - начальное значение диапазона
#fin_cal - конечное значение диапазона
#step - шаг диапазона
def table_former(init_val, fin_val, step):
    #1) открытие файла для записи (вторично, проще смотреть таблицу значений)
    result_tab = open('result_tab.txt', 'w')
    #2) определение числа знаков после запятой для значений диапазонов
    #если шаг - целочисленный, то значения будут также целочисленными
    #если шаг имеет меньше 5 знаков после запятой - считаем, сколько
    #если шаг имеет больше 5 знаков после запятой - берём пять знаков
    str_step = str(step)
    if step%1 == 0:
        dec_places = 0
    elif str_step.find('.'):
        dec_places = len(str_step.split('.')[1])
    else:
        dec_places = 5
    
    #Счётчик - номер элемента диапазона
    counter = 1

    #3) Определение полей таблицы и их размеров (второй print для вывода в файл)
    print(f'{"Number":<10}{"Value":<{dec_places + 10}}{"Result":<40}')
    print(f'{"Number":<10}{"Value":<{dec_places + 10}}{"Result":<40}',
                                                        file=result_tab)

    #4) построчная обработка таблицы
    #цикл прекращает работу, как только начальное значение (инкриментируемое)
    #становится больше конечного значения диапазона
    #счётчик (номер строки) инкрементируется также
    #если номер строки четен - вызывается функция even_max()
    #если номер строки нечетен - вызывается функция odd_max()
    #полученные данные выводятся print-ом в консоль как предусмотрено в задании
    #сначала номер строки -> затем число из диапазона -> затем значение функции для этого числа

    while init_val <= fin_val:
        if (counter%2 == 0):
            result = even_max(init_val)
        else:
            result = odd_min(init_val)
        print(f'{counter:<10}{init_val:<{dec_places + 10}.{dec_places}f}{result:<40}')
        print(f'{counter:<10}{init_val:<{dec_places + 10}.{dec_places}f}{result:<40}',
                                                                        file=result_tab)
        counter += 1
        init_val += step

    #5) после отработки функции файл закрывается, чтобы ненароком не внести в него изменения
    result_tab.close()  

#Функция main() - основная функция программы
#В ней происходит ввод значений для построения диапазона
#В ней же отлавливаются ошибки ввода и происходит вызов
#функции формирования таблицы table_former() от введённых значений
def main():
    #Цикл работает, пока не будут введены верные данныеъ
    #В случае ввода неверных данных выбрасывается исключение 
    #и сообщение о виде ошибки
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

    #Данные введены, отрисовывается таблица
    table_former(initial, final, step)

if __name__ == "__main__":
    main()