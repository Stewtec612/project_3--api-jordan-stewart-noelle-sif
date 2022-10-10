import requests
from pprint import pprint

power_animal_url = 'https://zoo-animal-api.herokuapp.com/animals/rand'

response = requests.get(power_animal_url)

data = response.json()

power_animal_name = data['name']


print(f'your power animal is: {power_animal_name}')