list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

sum_ = sum (list_)
print(sum_)

uni_znak = set (list_)
kol_uni_znak = len (uni_znak)
print(kol_uni_znak)



sred_arif_uni_znak = sum (uni_znak) / len (uni_znak)
sred_arif_uni_znak = round(sred_arif_uni_znak, 5)

print(sred_arif_uni_znak)


# TODO найти сумму, количество и среднее арифметическое уникальных чисел
