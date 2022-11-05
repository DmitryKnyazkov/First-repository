import random
import string

str_ = string.digits + string.ascii_uppercase + string.ascii_lowercase

def get_random_password(n=8) -> str:
    list_ = random.sample(str_, n)
    return "".join(list_)

     # TODO написать функцию генерации случайных паролей


print(get_random_password(15))

