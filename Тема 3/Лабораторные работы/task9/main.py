salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

zp_za_desyc_mes = 10

cikl = 0
spend_za_dev_mes = 0
spend_progres = spend
while cikl != 9:
    spend_progres = spend_progres + (spend_progres + increase)
    spend_za_dev_mes = spend_progres + spend_za_dev_mes
    cikl += 1

spend_za_desyc = spend_za_dev_mes + spend
need_money = spend_za_desyc -
    zp_za_des_mes = salary * months






# TODO Оформить решение

print(round(need_money))
