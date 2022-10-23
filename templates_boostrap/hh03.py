# 1. Как получить набор навыков
# # Поиск ваканси
# import requests
# import pprint
# import time
#
# url = 'https://api.hh.ru/vacancies'
#
# params = {
#     'text': 'NAME:Python',
#     # есть страницы т.к. данных много
#     'page': 1
# }
#
# result = requests.get(url, params=params).json()
#
# # список вакансий
# items = result['items']
# # pprint.pprint(items[0])
#
# for item in items[:10]:
#     url = item['url']
#
#     result = requests.get(url).json()
#
#     # pprint.pprint(result)
#     # 1. Ключевые навыки
#     print(result['key_skills'])
#     # 2. задержка между запросами
#     time.sleep(1)

# 3. Частотный анализ
key_skills = {}

skills = ['python', 'python', 'django', 'python', 'django', 'sql', 'sql', 'flask', 'sql']

for item in skills:
    # если он уже там есть
    if item in key_skills:
        # то мы его увеличиваем на 1
        key_skills[item] += 1
    else:
        # а если еще там нет
        # то мы его записываем со значением 1
        key_skills[item] = 1

print(key_skills)

# Сортировка по убыванию
# сортировка кортежей
result = sorted(key_skills.items(), key=lambda x: x[1], reverse=True)

print(result)


# словарь в объект
class Vacancy:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


vacancies = [{'name': 'python', 'salary': 200, 'url': ''}]

objs = []
for item in vacancies:
    vacancy = Vacancy(item['name'], item['salary'])
    objs.append(vacancy)
    print(vacancy.name)
