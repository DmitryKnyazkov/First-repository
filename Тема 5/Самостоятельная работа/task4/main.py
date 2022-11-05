import random
from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 10000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке
list_result = []

for count in counts:
    for _ in range(count):
        list_result.append(random.choice(coin))
        skolko_orlov = list_result.count("Орел")
        #print(skolko_orlov)
        skolko_reshka = list_result.count("Решка")
    print(list_result)

    if skolko_reshka < skolko_orlov:
        result = skolko_reshka / skolko_orlov
    else:
        result = skolko_orlov / skolko_reshka
    list_freq.append(result)


    # TODO подсчитать количество выпаданий орлов и решек

    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
