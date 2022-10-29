main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"""

def net_znakam(text):
    znaki = [".", ",", "!", "?", " ", "\n"]
    for znak in znaki:
        text = text.replace(znak,"")

    return text

main_str = net_znakam(main_str)

net_znakam(main_str)

def get_count_char(str_): # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_c = str_.lower()
    str_c.isalpha()

    dict_simvolov = {}
    SCHET = 0

    for simvol in str_c:
        if simvol in str_c:
            dict_simvolov[simvol] = dict_simvolov.setdefault(simvol, SCHET) + 1

    return dict_simvolov

print(get_count_char(main_str))

def v_procentah(dict_):
    summa_znacheniy = sum(dict_.values())
    kluchey_vsego = len(dict_)
    for kluch in dict_:
        dict_[kluch] = dict_[kluch]*100/summa_znacheniy
        dict_[kluch] = round(dict_[kluch], 1)
        print(kluch, "-", dict_[kluch], " %")
    return dict_

# print(v_procentah(get_count_char(main_str)))
