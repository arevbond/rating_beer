from transliterate import translit
import json

with open('ru_pivo.json') as file:
    data = json.load(file)



# def short_title(title):
#     new_name = ''
#     for word in title.split():
#         if word[0].isupper():
#             new_name += word + '-'
#     if new_name.split()[0] == 'Пивной':
#         new_name = new_name.split()
#         new_name[0] = 'Пивной напиток'
#         new_name = ''.join(new_name)
#     new_name = translit(new_name, language_code='ru', reversed=True)[:-1].lower()
#     if "'" in new_name:
#         new_name = new_name.replace("'", '')
#     return new_name
#
# for beer in data:
#     print(translit(beer.get('name'), language_code='ru', reversed=True).lower())

for beer in data:
    Beer.objects.create(title=beer.get('name'), description=beer.get('desc'), alcogol=beer.get('alcogol'), category_id=1, country_id=1)
