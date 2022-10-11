import json
import requests

with open('all_import.json') as file:
    data = json.load(file)

for i in range(len(data)):
    img_data = requests.get(data[i]['img']).content
    with open(f'all_beer_images/import/{i}.png', 'wb') as file:
        file.write(img_data)