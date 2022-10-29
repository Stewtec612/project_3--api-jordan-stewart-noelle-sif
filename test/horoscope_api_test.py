import requests
from pprint import pprint

users_sign = input('enter your zodiac sign: ').lower()

horoscope_url = f'https://ohmanda.com/api/horoscope/{users_sign}'

response = requests.get(horoscope_url)

data = response.json()

date = data['date']
zodiac_sign = data['sign']
horoscope = data['horoscope']





print(f'Today\'s date: {date}\n')
print(f'Zodiac sign: {zodiac_sign}\n')
pprint(horoscope)
