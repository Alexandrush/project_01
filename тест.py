# import random
# d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
# country, capital = random.choice(list(d.items()))
# print(country)

import random

my_dict = {
    'id': 1,
    'name': 'Bobbyhadz',
    'age': 30,
    'country': 'Chile',
    'city': 'Santiago',
}


random_keys = random.sample(list(my_dict), 2)
print(random_keys)  # 👉️ ['age', 'name']
