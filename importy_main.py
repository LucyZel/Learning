#1 možnost - zhlouhavější zápis

import importy_data
print(importy_data.my_data)

#2 možnost - používanější
from importy_data import my_data
print(my_data)

#3 možnost - moc se nepoužívá, je to matoucí
from importy_data import * #importuje se vše

#4 možnost - alias (jiný název)
import importy_data as d
print (d.my_data)