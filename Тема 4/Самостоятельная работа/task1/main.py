# TODO реализовать функцию
def remove_whitespace(str_):
    probel = " "
    kolichestvo_probelov = 0
    for znak in str_: # узнали максимальное количество пробелов, которое можем встретить в тексте
        if znak == probel:
            kolichestvo_probelov += 1

    for n in range(kolichestvo_probelov, 1, -1): # убираем пробелы
        probely = probel*n
        str_ = str_.replace(probely, " ")

    return str_

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
