# TODO решить с помощью list comprehension и распечатать его
import pprint

chislo = 16
list_dict = list(range(chislo))
def smena_znach(chislo=16):
    for i in list_dict:
        list_dict[i] = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    return list_dict

pprint.pprint(smena_znach(chislo))

