money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


bud = salary + money_capital
while bud >= spend:
    spend = spend + (spend * increase)
    money_capital = money_capital - (spend - salary)
    bud = salary + money_capital
    month += 1

print(month-2)
