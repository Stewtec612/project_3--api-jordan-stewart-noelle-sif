""" Make calls to Horoscope API, get horoscope based on the user's sign """

import requests
from get_user_info import get_user_info

user_sign = get_user_info()[1]


def get_horoscope(user_sign):
    # get a user horoscope based of the user's sign, that includes the date of the horoscope
    horoscope_url = f'https://ohmanda.com/api/horoscope/{user_sign}'
    response = requests.get(horoscope_url)
    horoscope_data = response.json()

    time = get_time_of_horoscope(horoscope_data)
    details = get_horoscope_details(horoscope_data)
    full_horoscope = [time, details]

    # for testing - we will still make some changes for formatting for the user
    print(full_horoscope)
    
    return full_horoscope

def get_time_of_horoscope(horoscope_data):
    # gets the current date from API
    the_date = horoscope_data['date']

    return the_date


def get_horoscope_details(horoscope_data):
    # gets users horoscope details from the API based off their input of their sign
    users_horoscope = horoscope_data['horoscope']

    return users_horoscope

get_horoscope(user_sign)

# for testing during development
# if __name__ == '__main__':
#     time, scope = get_horoscope('scorpio')
#     print(time, scope)