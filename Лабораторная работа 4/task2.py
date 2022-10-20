

def get_count_char(str_):
    str_1 = str_.lower()
    dict_symb = dict()
    for i in str_1:
        if dict_symb.get(i) == None:
                if i.isalpha() == True:
                    dict_symb.setdefault(i, 1)
        else:
            dict_symb[i] = dict_symb[i] + 1

    return dict_symb
    # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def PLOXO_SOSTAVLENOE_ZADANIE (dict_1):
    sum = 0
    for i in dict_1:
        sum=sum+dict_1[i]
    for i in dict_1:

        dict_1[i]=f"{format((dict_1[i]/sum)*100,'.2f')} %"

    return dict_1
PLOXO_SOSTAVLENOE_ZADANIE(get_count_char(main_str))
print(get_count_char(main_str))
