salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

zp_za_desyc_mes = salary * 10
spend_za_devy_mes = 0
cikl = 0
spend_progres = spend

while cikl != 9:
    spend_progres = spend_progres + (spend_progres * increase)
    spend_za_devy_mes = spend_progres + spend_za_devy_mes
    cikl += 1

spend_za_desyc_mes = spend_za_devy_mes + spend

need_money = spend_za_desyc_mes - zp_za_desyc_mes
# TODO Оформить решение

print(round(need_money))
