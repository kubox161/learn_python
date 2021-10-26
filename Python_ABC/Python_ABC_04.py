# Работаем с файлом IMDbnames_f.csv
# Вывести число людей, у которых количество детей больше, чем количество супругов.

import pandas as pd
fieldnames = ['imdb_name_id', 'name',
'height',
'date_of_birth',
'date_of_death',
'reason_of_death',
'spouses', 'divorces',
'spouses_with_children',
'children']
df = pd.read_csv('../IMDbnames_f.csv',
                 sep = '#',
                 names = fieldnames)

print(df) # печатаем результат