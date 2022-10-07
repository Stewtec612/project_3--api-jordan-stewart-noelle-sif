''' Rough draft code started in class 10/6/2022'''

import requests
from pprint import pprint 


try:
    planet_url = 'https://api.le-systeme-solaire.net/rest/bodies/'
    tarot_url = 'https://rws-cards-api.herokuapp.com/api/v1/cards'
    poetry_url = 'https://www.poetry.com/poetry_api.php'


    response = requests.get(planet_url)
    data = response.json()  
    pprint(data)

    planet_info = data['isPlanet'] ['name']  #getting objects from the website 
    print(planet_url)

    user_planet = (input('Enter your birthday: '))  #getting paramaters for birthday search
    # isolate month 
    # search API by birth month
    #"discoveryDate": "27/01/1908", in European format on API 
    # 

    print(f'Your {user_planet} matches {planet_info} ')

except Exception as e: 
    print(e)
    print('There was an error making the request')