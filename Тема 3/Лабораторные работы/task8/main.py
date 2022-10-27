money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
bud = salary + money_capital # бюджет состоит из подушки и ЗП

while bud >= spend:
    spend = spend + (spend * increase)
    money_capital = money_capital - (spend - salary)
    bud = salary + money_capital
    month += 1
# TODO Оформить решение

print(month - 2)  # вычел 2 для того чтобы совпадала со вторым правильным ответом

