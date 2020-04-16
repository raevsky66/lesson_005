# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from pprint import pprint

from district.central_street.house1.room1 import folks as folks_cs_h1_r1
from district.central_street.house1.room2 import folks as folks_cs_h1_r2
from district.central_street.house2.room1 import folks as folks_cs_h2_r1
from district.central_street.house2.room2 import folks as folks_cs_h2_r2

from district.soviet_street.house1.room1 import folks as folks_ss_h1_r1
from district.soviet_street.house1.room2 import folks as folks_ss_h1_r2
from district.soviet_street.house2.room1 import folks as folks_ss_h2_r1
from district.soviet_street.house2.room2 import folks as folks_ss_h2_r2

def get_tenants(list_tenants):
    tenants = ','
    # for tenant in list_tenants:
    #     tenants = tenants.join(tenant)
    return tenants.join(list_tenants)

str = get_tenants(folks_ss_h1_r1)
str = str + ','+ get_tenants(folks_ss_h1_r2)
str = str + ','+ get_tenants(folks_ss_h2_r1)
str = str + ','+ get_tenants(folks_ss_h2_r2)

str = str + ','+ get_tenants(folks_cs_h1_r1)
str = str + ','+ get_tenants(folks_cs_h1_r2)
str = str + ','+ get_tenants(folks_cs_h2_r1)
str = str + ','+ get_tenants(folks_cs_h2_r2)

# str = str.join(get_tenants(folks_cs_h1_r1))
print(str)

