def get_list_number_divisors(number):

    list_ = []
    for delitel in range(1, number +1):
        if number % delitel == 0:
            list_.append(delitel)
    return list_
      # TODO найти список делителей числа number


print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
