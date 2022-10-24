

import requests
import users_sign
#opens channel to the horoscope API
horoscope_url = f'https://ohmanda.com/api/horoscope/{users_sign}'

response = requests.get(horoscope_url)

horoscope_data = response.json()


def time():
    #gets the current date from API
    the_date = horoscope_data['date']

    return the_date


def horoscope_details():
    #gets users horoscope details from the API based off their input of their sign
    users_horoscope = horoscope_data['horoscope']

    return users_horoscope