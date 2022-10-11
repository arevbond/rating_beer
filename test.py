from transliterate import translit
import json

with open('all_import.json') as file:
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
#
# for beer in data:
#     Beer.objects.create(title=beer.get('name'), description=beer.get('desc'), alcogol=beer.get('alcogol'), category_id=2, country_id=beer.get('county'))

for i in range(len(data)):
    alcogol = data[i].get('alcogol')
    if len(alcogol) == 1:
        alcogol = int(alcogol)
    else:
        alcogol = float(alcogol.split()[0])
    Beer.objects.create(title=data[i].get('name'), description=data[i].get('desc'), alcogol=alcogol,category_id=2, country=data[i].get('county'), image=f'media/import/{i}.png', is_published=True)