ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    str_c = set(str_)
    for a in str_c:
        if a not in ALLOW_SYMBOLS:
            return False
        else:
            return True
    if not str_:
        return False


     # TODO проверить что в строку входят только символы 1 и 0


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
